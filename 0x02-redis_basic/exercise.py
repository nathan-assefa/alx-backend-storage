#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable, Any
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
    
    def get(self, key: str, fn: Callable = None) -> (Any, None):
        value = self._redis.get(key)
        if value and fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, lambda value: str(value))

    def get_int(self, key: int) -> Union[int, None]:
        return self.get(key, lambda value: int(value))
