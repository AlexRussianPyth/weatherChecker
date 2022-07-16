from weather.geolocator import get_coordinates
from weather.weatherapi import get_current_weather

query = 'Engels'


def main():
    # Get geographical coordinates by query
    location = get_coordinates(query)
    weather = get_current_weather(location)
    print(weather)


if __name__ == '__main__':
    main()
