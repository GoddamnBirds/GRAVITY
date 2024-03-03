import pymongo
from pymongo import MongoClient
import json
import datetime
import ast
import time 
from sms import send_sms
from pymongo.server_api import ServerApi
from config import url

cluster = MongoClient(url, server_api=ServerApi('1'))

dbnames = cluster.list_database_names()
db = cluster["Building"]
collection = []
collection.append(db["floor1"])
collection.append(db["floor2"])
collection.append(db["floor3"])

def setup():
    if "Building" in dbnames:
        return

    for i in range(0,3):
        for j in range(1,7):
            for k in range(1,9):
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
    
    return free

def removeVehicle(plateNo):
    for i in range(0,3):
        temp = collection[i].find_one({"plateNo":plateNo})
        if not(type(temp) is type(None)):
            free = temp["_id"]
            break

    unix_start_time = float(temp["unixTimeIn"]) 
    unix_end_time = time.mktime(datetime.datetime.now().timetuple())
    time_difference = unix_end_time - unix_start_time

    hours = time_difference // 3600
    minutes = (time_difference % 3600) // 60

    rate = (hours * 60) + (minutes * 1)
    print(f"user parked for {hours} hour(s) and {minutes} minute(s). Rate = {rate}")
    
    collection[i].update_one({"_id":free} , {"$set": {"isOccupied":False, "plateNo":"null", "driverNo":"null", "unixTimeIn":"null", "dateTimeIn":"null"}})
    return [free, hours, minutes, rate]

def getDuration(plateNo):
    for i in range(0,3):
        temp = collection[i].find_one({"plateNo":plateNo})
        if not(type(temp) is type(None)):
            break
    else:
        return -1

    unix_start_time = float(temp["unixTimeIn"]) 
    unix_end_time = time.mktime(datetime.datetime.now().timetuple())
    time_difference = unix_end_time - unix_start_time

    hours = time_difference // 3600
    minutes = (time_difference % 3600) // 60

    rate = (hours * 60) + (minutes * 1)
    print(f"user parked for {hours} hour(s) and {minutes} minute(s). Rate = {rate}")


#setup()
#addVehicle("TEST", "7337824488")
#removeVehicle("TEST")
#getDuration("TEST")