#!/usr/bin/env python3
import redis
import requests
''' Tracking url access '''


r = redis.Redis()


def get_page(url: str) -> str:
    """Tracking how many times a particular URL was accessed."""
    
    # Increment the access count in Redis
    count_key = f"count:{url}"
    current_count = r.get(count_key)
    if current_count is None:
        current_count = 0
    else:
        current_count = int(current_count)
    new_count = current_count + 1
    r.set(count_key, new_count)
    
    # Fetch the HTML content using requests
    resp = requests.get(url)
    
    # Cache the content with a 10-second expiration time
    cache_key = f"cached:{url}"
    r.setex(cache_key, 10, resp.text)
    
    return resp.text

if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
