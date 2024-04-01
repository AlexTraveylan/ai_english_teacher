"""This module contains the AppException class."""


class AppException(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, message):
        super().__init__(message)
