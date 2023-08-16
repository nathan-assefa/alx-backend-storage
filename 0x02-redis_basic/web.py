import redis
import requests
r = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """ tracking how many times a particular URL was accessed """ in the key
    r.set(f"cached:{url}", count)
    resp = requests.get(url)
    r.incr(f"count:{url}")
    r.setex(f"cached:{url}", 10, r.get(f"cached:{url}"))
    return resp.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
