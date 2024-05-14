#!/usr/bin/env python3
"""imported mosules"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    the function
    """
    return mongo_collection.find({"topics":  {"$in": [topic]}})
