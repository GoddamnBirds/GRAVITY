import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb+srv://GravityPark:Munches4Shawarma@gravitypark.aqseupl.mongodb.net/?retryWrites=true&w=majority&appName=GravityPark")
    db = client['test']
    collection = db['table']
    
    data = {
        "name": "gay",
        "age": 69
    }
    
    collection.insert_one(data)