from geolocator import get_coordinates
from weatherapi import get_weather

query = 'Engels'


def main():
    # Get geographical coordinates by query
    location = get_coordinates(query)
    weather = get_weather(location)

    print(weather.json())


if __name__ == '__main__':
    main()
