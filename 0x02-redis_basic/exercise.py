#!/usr/bin/env python3
"""
exercise.py
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(fn: Callable) -> Callable:
    """ decorator """

    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        """Wrapper func"""
        key = fn.__qualname__
        self.__redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(fn: Callable) -> Callable:
    """store the history of inputs and outputs for a particular function"""

    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self.__redis.rpush(method.__qualname__ + ":inputs", str(args))
        output = fn(self, *args, **kwargs)
        self.__redis.rpush(method.__qualname__ + ":outputs", str(output))
        return output
    return wrapper


class Cache:
    """store an instance of the Redis"""

    def __init__(self):
        """constructor"""
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """"takes a data argument and returns a string"""
        key = str(uuid.uuid4())
        self.__redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, int, bytes, float]:
        """Fetch data data"""
        data = self.__redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """fetch string"""
        return self.__redis.get(key, str)

    def get_int(self, key: str) -> int:
        """fetch integer"""
        return self.__redis.get(key, int)

    def replay(val: Cache):
        """display the history of calls of a particular function"""
        cls = val.__qualname__
        print("{} was called".format(
            cls, val.__self__.get(cls).decode("utf-8")))
        inputs = val.__self__.__redis.lrange("{}:inputs".format(cls), 0, -1)
        outputs = val.__self__.__redis.lrange("{}:outputs".format(cls), 0, -1)
        zipped = zip(inputs, outputs)
        for i, o in zipped:
            print("{}({}) -> ({})".format(
                    cls, i.decode("utf-8"), o.decode("utf-8")))
