from geolocator import get_coordinates


query = 'Engels'

if __name__ == '__main__':
    location = get_coordinates(query)
    print(location)
