from datetime import datetime
from typing import NamedTuple, List

import requests

from weather.geolocator import Coordinate
from weather.config import OPENWEATHER_API_KEY


Celsius = int

# TODO Add unit tests for this module
class Weather(NamedTuple):
    temperature: Celsius
    weather_type: str
    sunrise: datetime
    sunset: datetime
    city: str
    date: datetime


def get_current_weather(location: Coordinate) -> Weather:
    url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'lat': location.latitude,
        'lon': location.longitude,
        'appid': OPENWEATHER_API_KEY,
    }

    response = _get_openweather_response_json(params)

    return Weather(
        temperature=response['main']['temp'],
        weather_type=['weather'][0]['description'],
        sunrise=response['sys']['sunrise'],
        sunset=response['sys']['sunset'],
        city=response['name'],
    )


def get_weather_day_forecast(location: Coordinate, day: int) -> List[Weather]:
    """Returns a weather forecast for specific daytime of next 5 days"""

    url = 'https://api.openweathermap.org/data/2.5/forecast'

    params = {
        'lat': location.latitude,
        'lon': location.longitude,
        'appid': OPENWEATHER_API_KEY,
        'units': 'metric',
    }

    response = _get_openweather_response_json(url, params)

    if response['cod'] == '200':
        sunrise = response['city']['sunrise']
        sunset = response['city']['sunset']
        city = response['city']['name']

        weather_forecasts = []

        for forecast in response['list']:
            weather_forecasts.append(Weather(
                temperature=forecast['main']['temp'],
                weather_type=forecast['weather'][0]['description'],
                sunrise=sunrise,
                sunset=sunset,
                city=city,
                date=forecast['dt_txt']
            ))
        return weather_forecasts

    return {'error': 'Get some error'}


def _get_openweather_response_json(url, params: dict) -> dict:
    """Get weather JSON from OpenWeather API"""
    response = requests.get(url, params=params).json()

    return response

