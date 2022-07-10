import pathlib
import os

from dotenv import load_dotenv

from geolocator import get_coordinates

load_dotenv(os.path.join(pathlib.Path(__file__).parent.absolute(), '.env'))

API_KEY = os.getenv('API_KEY')

query = 'Engels'

if __name__ == '__main__':
    location = get_coordinates(query)
