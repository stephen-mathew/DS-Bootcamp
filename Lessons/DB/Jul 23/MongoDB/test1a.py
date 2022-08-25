import pymongo
import urllib.parse

mongo_uri = "mongodb+srv://steve:" + urllib.parse.quote("Steve@123") + "@clustersteve.j5khq.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_uri)

db = client.test
print(db)

database = client["myinfo"]
collection = database["steve"]
record = collection.find()

# for i in record:
#     print(i)

# data = collection.find({"companyName":"iNeuron"})
data = collection.find({"courseOffered":{"$gt":"E"}})
for i in data:
    print(i)

