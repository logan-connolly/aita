class DoesNotExist(Exception):
    """Raise when a searched object is not found"""


class AlreadyExists(Exception):
    """Raise when an object passed to application already exists"""
