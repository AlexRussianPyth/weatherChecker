import os
import pathlib

from dotenv import load_dotenv

load_dotenv(os.path.join(pathlib.Path(__file__).parent.parent.absolute(), '.env'))

PROJECT_NAME = 'Weather API'

UVICORN_RELOAD = os.getenv('UVICORN_RELOAD', 'False') == 'True'
