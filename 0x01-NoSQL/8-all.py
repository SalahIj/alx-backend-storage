#!/usr/bin/env python3
"""imported modules"""


def list_all(mongo_collection):
    """the function"""
    return [doc for doc in mongo_collection.find()]
