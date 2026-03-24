import requests
import random

http_ok: int = 200


def get_jokes() -> str:
    url: str = "https://api.freeapi.app/api/v1/public/randomjokes"

    querystring = {
        "limit": "10",
        "query": "science",
        "inc": "categories%2Cid%2Ccontent",
        "page": "1",
    }

    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers, params=querystring)
    payload = response.json()

    if payload["statusCode"] == http_ok:
        jokes: list[dict[str, str]] = payload["data"]["data"]

    else:
        raise Exception
    return random.choice(jokes)["content"]


def main():
    jokes = get_jokes()
    print(jokes)


if __name__ == "__main__":
    main()
