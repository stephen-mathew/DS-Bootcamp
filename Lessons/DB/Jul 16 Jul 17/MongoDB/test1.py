import pymongo
import urllib.parse

mongo_uri = "mongodb+srv://steve:" + urllib.parse.quote("Steve@123") + "@clustersteve.j5khq.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_uri)

db = client.test
print(db)

d = {
    "name": "Steve",
    "email":"steve@domain.com",
    "surname":"Matt"
}
db1 = client["mongotest"]
coll = db1['test']
coll.insert_one(d)