import mysql.connector as conn

mydb = conn.connect(host = "localhost",user="root",password="Steve@123")
cursor = mydb.cursor()
# cursor.execute("show databases")
# cursor.execute("create database steve")
# cursor.execute("show databases")
# cursor.execute("create table steve.ineuron(employee_id int(10), emp_name varchar(80), emp_mailid varchar(80), "
#                "emp_salary int(7), emp_attendance int(3))")
q2= cursor.execute('select * from steve.ineuron')
# print(cursor.fetchall())
print(q2)