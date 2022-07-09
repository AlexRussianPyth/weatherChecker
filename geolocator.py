from geopy.geocoders import Nominatim

def get_coordinates(query: str) -> dict:
    """Function use string query to achieve address and geo coordinates of place"""
    locator = Nominatim(user_agent="GetLoc")

    # entering the location name
    get_loc = locator.geocode(query)

    location = {
        'address': get_loc.address,
        'lat': get_loc.latitude,
        'lon': get_loc.longitude,
    }

    return location







