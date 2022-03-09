"""
Module with HTTP client  class
"""
import requests
from typing import Optional


class HttpClient:
    """
    A class for making HTTP requests
    """

    @staticmethod
    def get_request(url: str, headers: Optional[dict] = None, params: Optional[dict] = None):
        """
        Sends a GET request
        """
        return requests.get(url, headers=headers, params=params)

    @staticmethod
    def post_request(url: str, headers: Optional[dict] = None, data: Optional[dict] = None, args=None):
        """
        Sends a POST request
        """
        return requests.post(url, headers=headers, data=data, args=args)

    @staticmethod
    def put_request(url: str, headers: Optional[dict] = None, data: Optional[dict] = None):
        """
        Sends a PUT request
        """
        return requests.put(url, headers, data=data)

    @staticmethod
    def delete_request(url: str, headers: Optional[dict] = None, data: Optional[dict] = None, args=None):
        """
        Sends a DELETE request
        """
        return requests.delete(url, headers=headers, data=data, args=args)