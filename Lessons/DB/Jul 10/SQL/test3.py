import mysql.connector as conn

mydb = conn.connect(host = "localhost",user="root",password="Steve@123")
cursor = mydb.cursor()

cursor.execute("select employee_id,emp_mailid from steve.ineuron")
# print(cursor.fetchall()) # this will only display the first row result
l = []
for i in cursor.fetchall():
    print(i)
    l.append(i)

print(l)
print(type(l[0]))
