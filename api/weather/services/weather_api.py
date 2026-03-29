import requests
from api.weather.config.env import API_KEY

HTTP_OK: int = 200
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(location: str, aqi: str):

    parameters = {"key": API_KEY.strip(), "q": location, "aqi": aqi}

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/115.0.0.0 Safari/537.36",
        "Accept": "application/json",
    }

    res = requests.get(BASE_URL, params=parameters)

    if res.status_code == HTTP_OK:
        payload = res.json()
        return payload
    else:
        print(f"Request failed with status code {res.status_code}")
