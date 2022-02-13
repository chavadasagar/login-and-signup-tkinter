import sqlite3

from numpy import true_divide

con = sqlite3.connect("User.db")

def createTable():
    con.execute("create table if not exists std(uid INTEGER PRIMARY KEY AUTOINCREMENT,name text,username text,password text)")
    con.commit()
    
def saveUser(name,username,password):
    data = (name,username,password)
    con.execute("insert into std(name,username,password) values(?,?,?)",data)
    con.commit()
    
def updateUser(uid,name,username,password):
    data = (name,username,password,uid)
    con.execute("update std set name=? ,username=?,password=? where uid=?",data)
    con.commit()
    
def deleteUser(uid):
    data = (uid)
    con.execute("delete from std where uid='"+uid+"'")
    con.commit()

def getalluser():
    cur = con.execute("select * from std")
    data = cur.fetchall()
    return data

def getUsernamePasswordByUser(username,password):
    val = (username,password)
    cur = con.execute("select * from std where username=? and password=?",val)
    data = cur.fetchall()
    if len(data) == 0:
        return False
    else:
        return True

def getUser(uid):
    cur = con.execute("select * from std where uid='"+uid+"'")
    data = cur.fetchall()
    return data

def search(search):
    cur = con.execute("select * from std where uid like '%"+search+"%' or name like '%"+search+"%' or username like '%"+search+"%'")
    data = cur.fetchall()
    return data
    
def clear():
    con.execute("delete from std where 1=1")
    con.commit()

createTable()