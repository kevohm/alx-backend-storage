#!/usr/bin/python3
""" provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    logsCount = db.nginx.count()
    data = ["GET","POST","PATCH","DELETE","PUT"]
    for i in data:
        c = db.nginx.find({"method":i}).count()
        print("\tmethod {}: {}".format(i,c))
