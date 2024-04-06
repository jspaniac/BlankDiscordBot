class TimeoutError(Exception):
    """
    A timeout exception for repeat request handling
    """
    pass


class InvalidResponse(Exception):
    """
    An exception for when users provide invalid responses to requests
    """
    pass
