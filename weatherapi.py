import os
import pathlib

import requests
from dotenv import load_dotenv

from geolocator import Coordinate

load_dotenv(os.path.join(pathlib.Path(__file__).parent.absolute(), '.env'))

API_KEY = os.getenv('API_KEY')
url = 'https://api.openweathermap.org/data/2.5/weather'


def get_weather(location: Coordinate):
    # Request response from OpenWeather API by geolocation
    params = {
        'lat': location.latitude,
        'lon': location.longitude,
        'appid': API_KEY,
    }
    response = requests.get(url, params=params)
    return response
