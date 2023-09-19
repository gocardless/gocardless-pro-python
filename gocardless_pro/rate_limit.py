from functools import wraps


def update_rate_limit(method):
    """Wrap all fetch methods in this decorator to update the client's
    ratelimit object with remaining requests available.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        response = method(self, *args, **kwargs)
        self.rate_limit.update_from_response(response)
        return response
    return wrapper


class RateLimit:

    def __init__(self):
        self.limit = None
        self.remaining = None
        self.reset = None

    def update_from_response(self, response):
        """Reads the remaining ratelimit from the response and updates
        the remaining attribute.
        Args:
          response (requests.Response): A requests ``Response`` object.
        """
        remaining = response.headers.get('ratelimit-remaining')
        if remaining:
            self.remaining = int(remaining)

        limit = response.headers.get('ratelimit-limit')
        if limit:
            self.limit = int(limit)

        self.reset = response.headers.get('ratelimit-reset')
