import requests


def init_headers():
    
    with open("cookie.txt", "r", encoding="utf-8") as f:
        cookie = f.read()

    Headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    }

    Headers["Cookie"] = cookie

    return Headers




