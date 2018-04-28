import sqlite3

con = sqlite3.connect('D:\\test.db')
cur = con.cursor()
cur.execute('drop table person')
cur.execute('create table person (id integer PRIMARY KEY , NAME VARCHAR(255), age INTEGER )')

cur.execute('insert into person VALUES (?,?,?)',(0,"qiye",20))
con.commit()
cur.execute('insert into person VALUES (?,?,?)',(1,"qiye2",21))
con.commit()
cur.execute('select * from person')
res = cur.fetchall()
for line in res:
    print line
cur.execute('select * from person')
res1 = cur.fetchone()
print res1
con.close()