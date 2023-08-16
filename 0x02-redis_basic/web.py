#!/usr/bin/env python3
import redis
import requests
from functools import wraps
from typing import Callable
''' Tracking url access '''


radis = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """ tracking the number of calls """

    @wraps(method)
    def wrapper(url):
        radis.incr(f"count:{url}")
        cached_html = radis.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        radis.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_calls
def get_page(url: str) -> str:
    """Tracking how many times a particular URL was accessed."""
    req = requests.get(url)
    return req.text
