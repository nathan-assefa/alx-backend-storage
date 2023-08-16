#!/usr/bin/env python3
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Any
""" Basic operations of redis """


def count_calls(method: Callable) -> Callable:
    ''' A decorator that counts a function call'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    ''' Sending datas to redis using RPUSH '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # let us first compile the keys
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Sending the input in the redis list
        self._redis.rpush(input_key, str(args))

        # now call the original function and save the result
        result = method(self, *args, **kwargs)

        # Then send the result to the redis output list
        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


class Cache:
    def __init__(self):
        """ intializing attributes """
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    @call_history
    @count_calls
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
