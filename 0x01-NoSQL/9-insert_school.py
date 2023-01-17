#!/usr/bin/python3
""" insert to school """

def insert_school(mongo_collection, **kwargs):
    """return id of inserted doc """
    return mongo_collection.insert_one(kwargs).inserted_id
