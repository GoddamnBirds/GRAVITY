import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    cluster = MongoClient("mongodb+srv://GravityPark:Munches4Shawarma@gravitypark.aqseupl.mongodb.net/?retryWrites=true&w=majority&appName=GravityPark")
    db = cluster.test
    result = db.command('ismaster')
    if result['ok']:
        print("MongoDB connected successfully!")
    else:
        print("MongoDB connection failed.")
except ConnectionFailure:
    print("MongoDB connection failed.")


db = cluster["test"]
collection = db["test"]

thing = {"_id":1, "name":"name"}

collection.insert_one(thing)