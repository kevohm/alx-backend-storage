#!/usr/bin/python3
"""lists all documents in a collection"""

def list_all(mongo_collection):
    """Return an empty list if no document in the collection"""
    if mongo_collection is not None:
        return mongo_collection.find()
