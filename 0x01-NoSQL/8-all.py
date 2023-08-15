#!/usr/bin/env python3
""" Listing all documents """
import pymongo


def list_all(mongo_collection) -> list:
    """ This function returns the list of all documnets
    from the collection named school """
    if not mongo_collection.find():
        return []
    return list(mongo_collection.find())
