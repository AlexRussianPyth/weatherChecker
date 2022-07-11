import os
import pathlib
from datetime import datetime
from enum import Enum
from typing import NamedTuple

import requests
from dotenv import load_dotenv

from geolocator import Coordinate

load_dotenv(os.path.join(pathlib.Path(__file__).parent.absolute(), '.env'))

API_KEY = os.getenv('API_KEY')
url = 'https://api.openweathermap.org/data/2.5/weather'

Celsius = int


class WeatherType(Enum):
    THUNDERSTORM = 'Гроза'
    DRIZZLE = 'Изморозь'
    RAIN = 'Дождь'
    SNOW = 'Снег'
    CLEAR = 'Ясно'
    FOG = 'Туман'
    CLOUDS = 'Облачно'


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(location: Coordinate) -> Weather:

    response = _get_openweather_response(location)

    return Weather(
        temperature=response['main']['temp'],
        weather_type=WeatherType.RAIN,
        sunrise=response['sys']['sunrise'],
        sunset=response['sys']['sunset'],
        city=response['name'],
    )

def _get_openweather_response(location: Coordinate) -> dict:
    """Get weather json from OpenWeather API"""
    # Request response from OpenWeather API by geolocation
    params = {
        'lat': location.latitude,
        'lon': location.longitude,
        'appid': API_KEY,
    }
    response = requests.get(url, params=params).json()

    return response


