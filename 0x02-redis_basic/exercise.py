#!/usr/bin/env python3
"""
exercise.py
"""
import redis
import uuid
from typing import Union, Optional, Callable



def count_calls(fn:Callable)->Callable:
    """ decorator """
    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        """Wrapper func"""
        key = fn.__qualname__
        self.__redis.incr(key)
        return method(self, *args,**kwargs)
    print("hello")
    return wrapper


class Cache:
    """store an instance of the Redis client as a private variable named _redis"""
    def __init__(self):
        """constructor"""
        self.__redis = redis.Redis()
        self.__redis.flushdb()


    @count_calls
    def store(self, data: Union[str, bytes, int, float])-> str:
        """"takes a data argument and returns a string"""
        key = str(uuid.uuid4())
        self.__redis.set(key,data)
        return key
    
    
    def get(self, key:str,fn:Optional[Callable]=None)->Union[str, int, bytes, float]:
        """Fetch data data"""
        data = self.__redis.get(key)
        if fn:
            return fn(data)
        return data


    def get_str(self, key:str)->str:
        """fetch string"""
        return self.__redis.get(key, str)


    def get_int(self, key:str)->int:
        """fetch integer"""
        return self.__redis.get(key, int)

