import os
import pathlib
from datetime import datetime
from typing import NamedTuple

import requests
from dotenv import load_dotenv

from geolocator import Coordinate

load_dotenv(os.path.join(pathlib.Path(__file__).parent.absolute(), '.env'))

API_KEY = os.getenv('API_KEY')
url = 'https://api.openweathermap.org/data/2.5/weather'

Celsius = int

class Weather(NamedTuple):
    temperature: Celsius
    weather_type: str
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(location: Coordinate) -> Weather:
    # Request response from OpenWeather API by geolocation
    params = {
        'lat': location.latitude,
        'lon': location.longitude,
        'appid': API_KEY,
    }
    response = requests.get(url, params=params)

    return response
