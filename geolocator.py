from geopy.geocoders import Nominatim
from pydantic import BaseModel


class Coordinate(BaseModel):
    latitude: float
    longitude: float


def get_coordinates(query: str) -> Coordinate:
    """Function use string query to achieve address and geo coordinates of place"""
    locator = Nominatim(user_agent="GetLoc")

    # entering the location name
    get_loc = locator.geocode(query)

    location = Coordinate(latitude=get_loc.latitude, longitude=get_loc.longitude)

    return location
