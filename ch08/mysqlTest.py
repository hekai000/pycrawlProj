import MySQLdb

con = MySQLdb.connect(host="localhost", user="root", passwd="root123", db="test",port=3306, charset="utf8")

cur = con.cursor()
#cur.execute('create table person (id int not null auto_increment PRIMARY key,name VARCHAR(20),age int)')
cur.execute("insert into person (name, age) VALUES (%s,%s)", ('qiye', 20))
con.commit()
cur.execute('select * from person')
res = cur.fetchall()
for line in res:
    print line
