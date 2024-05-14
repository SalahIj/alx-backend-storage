#!/usr/bin/env python3
""" imported modules """


def insert_school(mongo_collection, **kwargs):
    """ the function """
    return mongo_collection.insert(kwargs)
