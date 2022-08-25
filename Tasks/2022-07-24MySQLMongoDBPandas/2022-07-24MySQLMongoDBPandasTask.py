import mysql.connector as conn

mydb = conn.connect(host="localhost",user="root",password="Steve@123")
cursor = mydb.cursor()

cursor.execute("create table if not exists Attribute( \
Price varchar(30), \
Rating float,\
Size varchar(30),\
Season varchar(30),\
Neckline varchar(30),\
SleeveLength varchar(30),\
waiseline varchar(30),\
Material varchar(30),\
FabricType varchar(30),\
Decoration varchar(30),\
PatternType varchar(30),\
Recommendation boolean\
)
")