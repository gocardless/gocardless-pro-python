from functools import wraps


def ratelimitupdate(method):
    """Wrap all fetch methods in this decorator to update the client's
    ratelimit object with remaining requests available.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        response = method(self, *args, **kwargs)
        self.ratelimit.update_from_response(response)
        return response
    return wrapper


class RateLimit:

    def __init__(self, remaining):
        self.remaining = remaining

    def update_from_response(self, response):
        """Reads the remaining ratelimit from the response and updates
        the remaining attribute.

        Args:
          response (requests.Response): A requests ``Response`` object.
        """
        remaining = response.headers._store.get('ratelimit-remaining')[1]
        self.remaining = int(remaining)