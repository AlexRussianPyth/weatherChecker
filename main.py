from weather.geolocator import get_coordinates
from weather.weatherapi import get_weather_day_forecast
from weather.config import LOCATION_NAME


def main():
    # Get geographical coordinates by query
    location = get_coordinates(query=LOCATION_NAME)
    weather = get_weather_day_forecast(location=location, day='monday')
    print(weather)


if __name__ == '__main__':
    main()
