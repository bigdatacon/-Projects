"""Implements connector to Movie Async API for search info about movies, people, genres."""
from http import HTTPStatus
from typing import List, Optional, Tuple
from uuid import UUID
import requests


class SearchConnector:
    def __init__(self, url):
        self._url = url

    def get_response(self, path: str, query: Optional[dict] = None) -> Optional[dict]:
        response = requests.get(self._url + path, params=query)
        return response


    def get_film_by_uuid(self, film_uuid: UUID):
        response = self._get_response(f"film/{film_uuid}")
        if response.status_code != HTTPStatus.OK:
            return None

        return response.json()

    def get_all_films(self) -> Optional[dict]:
        response = self._get_response(f"return_film_data/")
        if response.status_code != HTTPStatus.OK:
            return None

        return response.json()