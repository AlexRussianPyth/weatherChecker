class CantGetCoordinates(Exception):
    """Program can't get GPS coordinates"""
    pass


class APIServiceError(Exception):
    """Program can't get current weather from API"""
    pass
