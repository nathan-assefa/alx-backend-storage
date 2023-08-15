#!/usr/bin/env python3
""" Write a Python function that inserts a new
document in a collection based on kwargs """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ This function inserts documents into mongo_collection """
    new_document = mongo_collection.insert_one(kwargs)

    ''' The insert_one() method returns a InsertOneResult object,
    which is assigned to the variable new_document. '''

    return new_document.inserted_id
