import pymongo
from pymongo import MongoClient
import json
import datetime
import ast
import time 
from sms import send_sms


cluster = MongoClient("mongodb://localhost:27017/")
dbnames = cluster.list_database_names()
db = cluster["Building"]
collection = []
collection.append(db["floor1"])
collection.append(db["floor2"])
collection.append(db["floor3"])

def setup():
    if "Building" in dbnames:
        return
    print("1")

    for i in range(0,3):
        for j in range(1,5):
            for k in range(1,15):
                date_time = datetime.datetime.now()
                unix_time = time.mktime(date_time.timetuple())
                text = '{"_id":"%s,%s", "isOccupied":False, "plateNo":"null", "driverNo":"null", "unixTimeIn":"null", "dateTimeIn":"null"}' % (j, k)
                res = ast.literal_eval(text)
                collection[i].insert_one(res)

def addVehicle(license, phoneNo):
    free = ""
    for i in range(0,3):
        temp = collection[i].find_one({"isOccupied":False})
        if not(type(temp) is type(None)):
            free = temp["_id"]
            floor = i + 1
            break
    else:
        return -1
    date_time = datetime.datetime.now()
    unix_time = time.mktime(date_time.timetuple())
    collection[i].update_one({"_id":free} , {"$set": {"isOccupied":True, "plateNo":license, "driverNo":phoneNo, "unixTimeIn":unix_time, "dateTimeIn":date_time}})
    send_sms(phoneNo, free, floor)
    return 0

def removeVehicle(plateNo):
    for i in range(0,3):
        temp = collection[i].find_one({"plateNo":plateNo})
        if not(type(temp) is type(None)):
            free = temp["_id"]
            floor = i + 1
            break
    collection[i].update_one({"plateNo":plateNo}, {"$set": {"isOccupied":False, "plateNo":license, "driverNo":phoneNo, "unixTimeIn":unix_time, "dateTimeIn":date_time}})


setup()
addVehicle("ABCDEFG", "7738812438")