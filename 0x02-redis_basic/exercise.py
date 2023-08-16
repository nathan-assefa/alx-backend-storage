#!/usr/bin/env python3
import redis
import uuid
from typing import Union
""" Basic operations of redis """


class Cache:
    def __init__(self):
        """ intializing attributes """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ storing key value pair in the redis serever """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
