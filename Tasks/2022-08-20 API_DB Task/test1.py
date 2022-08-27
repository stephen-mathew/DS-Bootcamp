import mysql.connector as conn

mydb = conn.connect(host = "localhost",user="root",password="Steve@123")
cursor = mydb.cursor()

query = "insert into steve.bank_details1 values (37,'product manager','single','tertiary','NULL',2,'yes','yes','unknown',5,'may',76,1,-1,0,'unknown','no')"
cursor.execute(query)

mydb.commit()