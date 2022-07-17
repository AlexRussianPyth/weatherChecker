import pathlib
import os

from dotenv import load_dotenv

load_dotenv(os.path.join(pathlib.Path(__file__).parent.absolute(), '../.env'))


OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
LOCATION_NAME = os.getenv('LOCATION_NAME')
