#!/usr/bin/env python3
"""
function to lists all documents in a collection
"""

def list_all(mongo_collection):
    """
    prototype: def list_all(mongo_collection)
    Returns an empty list if document is empty
    """
    documentList = mongo_collection.find()
    return documentList
