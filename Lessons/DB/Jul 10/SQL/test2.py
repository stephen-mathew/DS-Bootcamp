import mysql.connector as conn

mydb = conn.connect(host = "localhost",user="root",password="Steve@123")
cursor = mydb.cursor()
s = "insert into steve.ineuron values(101,'steve matt','steve@domain.com',100,90)"
s01 = "insert into steve.ineuron values(102,'steve matt2','steve@domain.com',102,90)"
s02 = "insert into steve.ineuron values(103,'steve matt3','steve@domain.com',101,92)"
cursor.execute(s01)
cursor.execute(s02)
mydb.commit()

cursor.execute("select * "
               "from steve.ineuron")
for i in cursor.fetchall():
    print(i)