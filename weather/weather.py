from typing import List

from weather.geolocator import get_coordinates
from weather.weatherapi import Weather, get_weather_day_forecast
from weather.config import LOCATION_NAME


def get_forecast(location_name=LOCATION_NAME) -> List[Weather]:
    # Get geographical coordinates by query
    location = get_coordinates(query=LOCATION_NAME)
    weather = get_weather_day_forecast(location=location)
    return weather
