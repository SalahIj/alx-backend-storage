#!/usr/bin/env python3
"""imported  modules"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    the fuction
    """
    return mongo_collection.update_many({
            "name": name
        },
        {
            "$set": {
                "topics": topics
            }
        })
