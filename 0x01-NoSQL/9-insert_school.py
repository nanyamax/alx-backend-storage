#!/usr/bin/env python3
"""
function that inserts a new doc in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Prototype: def insert_school(mongo_collection, **kwargs)
    """
    new_kwargs = mongo_collection.insert_one(kwargs)
    return new_kwargs.inserted_id
