#!/usr/bin/env python3
"""Imported modules"""
import redis
from uuid import uuid4
from functools import wraps
from typing import Any, Callable, Optional, Union


class Cache:
    """The class definition"""
    def __init__(self) -> None:
        """The __init__ function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes,  int,  float]) -> str:
        """Store method"""
        key = str(uuid4())
        client = self._redis
        client.set(key, data)
        return key
