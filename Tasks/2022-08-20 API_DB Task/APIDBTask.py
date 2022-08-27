import mysql.connector as conn
import pymongo
import urllib.parse
from flask import Flask, request, jsonify

app = Flask(__name__)

mydb = conn.connect(host = "localhost",user="root",password="Steve@123")
cursor = mydb.cursor()

mongo_uri = "mongodb+srv://steve:" + urllib.parse.quote("Steve@123") + "@clustersteve.j5khq.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_uri)
database = client["Bank"]
collection = database["Bank"]

## Insert a record to SQL from API
@app.route('/insert_sql',methods=['GET','POST'])
def insert_sql():
    if (request.method == 'POST'):
        age = request.json['age']
        job = request.json['job']
        marital = request.json['marital']
        education = request.json['education']
        default = request.json['default']
        balance = request.json['balance']
        housing = request.json['housing']
        loan = request.json['loan']
        contact = request.json['contact']
        day = request.json['day']
        month = request.json['month']
        duration = request.json['duration']
        campaign = request.json['campaign']
        pdays = request.json['pdays']
        previous = request.json['previous']
        poutcome = request.json['poutcome']
        y = request.json['y']

        query = "insert into steve.bank_details1 values ("+str(age)+",'"+job+"','"+marital+"','"+education+"','"+default+"'," \
                ""+str(balance)+",'"+housing+"','"+loan+"','"+contact+"',"+str(day)+",'"+month+"',"+str(duration)+","+str(campaign)+"," \
                ""+str(pdays)+","+str(previous)+",'"+poutcome+"','"+y+"')"
        cursor.execute(query)
        mydb.commit()
        return jsonify(str(query))

## Insert a record to Mongo DB from API
@app.route('/insert_mongo',methods=['GET','POST'])
def insert_mongo():
    if (request.method == 'POST'):
        data = request.json
        feedback = collection.insert_one(data)
        return jsonify(str(feedback))

## Update a record to SQL from API
@app.route('/update_sql',methods=['GET','POST'])
def update_sql():
    if (request.method == 'POST'):
        age = request.json['age']
        job = request.json['job']

        query = "update steve.bank_details1 set job='"+job+"' where age="+str(age)
        cursor.execute(query)
        mydb.commit()
        return jsonify(str(query))

## Update a record to Mongo DB from API
@app.route('/update_mongo',methods=['GET','POST'])
def update_mongo():
    if (request.method == 'POST'):
        age = request.json['age']
        job = request.json['job']

        feedback = collection.update_one({"age": age}, {"$set" : {"job" : job}})
        return jsonify(str(feedback))

## Delete a record to SQL from API
@app.route('/delete_sql',methods=['GET','POST'])
def delete_sql():
    if (request.method == 'POST'):
        age = request.json['age']

        query = "delete from steve.bank_details1 where age=" + str(age)
        cursor.execute(query)
        mydb.commit()
        return jsonify(str(query))

## Delete a record to Mongo DB from API
@app.route('/delete_mongo',methods=['GET','POST'])
def delete_mongo():
    if (request.method == 'POST'):
        age = request.json['age']

        feedback = collection.delete_one({"age": age})
        return jsonify(str(feedback))

## Fetch a record from SQL from API
@app.route('/fetch_sql',methods=['GET','POST'])
def fetch_sql():
    if request.method == 'POST':
        age = request.json['age']
        cursor.execute("select * from steve.bank_details1 where age="+str(age))
        l = cursor.fetchall()
        return jsonify(str(l[0]))

## Fetch a record from Mongo DB from API
@app.route('/fetch_mongo',methods=['GET','POST'])
def fetch_mongo():
    if request.method == 'POST':
        age = request.json['age']
        d = collection.find({"age": age})
        return jsonify(str(d[0]))

if __name__ == '__main__':
    app.run()