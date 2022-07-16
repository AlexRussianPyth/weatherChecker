import os
import pathlib
from datetime import datetime
from enum import Enum
from typing import NamedTuple

import requests
from dotenv import load_dotenv

from weather.geolocator import Coordinate

load_dotenv(os.path.join(pathlib.Path(__file__).parent.absolute(), '../.env'))

API_KEY = os.getenv('OPENWEATHER_API_KEY')
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


def get_current_weather(location: Coordinate) -> Weather:

    params = {
        'lat': location.latitude,
        'lon': location.longitude,
        'appid': API_KEY,
    }

    response = _get_openweather_response(params)

    return Weather(
        temperature=response['main']['temp'],
        weather_type=WeatherType.RAIN,
        sunrise=response['sys']['sunrise'],
        sunset=response['sys']['sunset'],
        city=response['name'],
    )


def get_weather_day_forecast(location: Coordinate) -> Weather:
    params = {
        'lat': location.latitude,
        'lon': location.longitude,
    }


def _get_openweather_response(params: dict) -> dict:
    """Get weather JSON from OpenWeather API"""
    response = requests.get(url, params=params).json()

    return response

