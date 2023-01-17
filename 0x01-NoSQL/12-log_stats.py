#!/usr/bin/env python3
""" 12-log_stats.py """
from pymongo import MongoClient


def main():
    """Python script that provides some stats"""

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx
    print(f"{nginx.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(f"""\tmethod {method}: {nginx.count_documents(
                {"method": method})}"""
              )
    print(f"""{nginx.count_documents({
            "method": "GET", "path": "/status"})} status check"""
          )


if __name__ == "__main__":
    main()
