from geopy.geocoders import Nominatim
from geopy.exc import GeopyError
from pydantic import BaseModel

from weather.exceptions import CantGetCoordinates


class Coordinate(BaseModel):
    latitude: float
    longitude: float


def get_coordinates(query: str) -> Coordinate:
    """Function use string query to achieve address and geo coordinates of place"""
    locator = Nominatim(user_agent="GetLoc")

    # entering the location name
    try:
        get_loc = locator.geocode(query)
    except GeopyError:
        raise CantGetCoordinates

    return Coordinate(latitude=get_loc.latitude, longitude=get_loc.longitude)
