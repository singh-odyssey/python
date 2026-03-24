import requests 
import os  
import pathlib

HTTP_OK: int = 200

def get_api():


api_key: str =os.getenv("API_KEY") 

print(api_key)

def get_weather_data(api_key: str) -> None: ...
