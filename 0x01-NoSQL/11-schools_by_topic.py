#!/usr/bin/env python3
"""
Returns list of schools having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    topic: string will be topic searched
    """
    return mongo_collection.find({"topic": topic})
