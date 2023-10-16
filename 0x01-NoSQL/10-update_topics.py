#!/usr/bin/env python3
"""
changes all topics of a school based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    prototype: def update_topics(mongo_collection, name, topics)
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
