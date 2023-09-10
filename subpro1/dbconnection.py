import pymysql
db=pymysql.connect(user="root",password="",host="localhost",database="amazon")
def addrow(sql):
    cur=db.cursor()
    cur.execute(sql)
    db.commit()
def selone(sql):
    cur=db.cursor()
    cur.execute(sql)
    value=cur.fetchone()
    return value
def selall(sql):
    cur=db.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    return data
def delrow(sql):
    cur=db.cursor()
    cur.execute(sql)
    db.commit()
def uprow(sql):
    cur=db.cursor()
    cur.execute(sql)
    db.commit()