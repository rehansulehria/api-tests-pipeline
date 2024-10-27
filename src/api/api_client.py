from http.client import responses

import requests

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint: str) -> dict:
        response = requests.get(f"{self.base_url}{endpoint}")
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, data: dict) -> dict:
        response = requests.post(f"{self.base_url}{endpoint}", json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint: str) -> requests.Response:
        response = requests.delete(f"{self.base_url}{endpoint}")
        response.raise_for_status()
        return response

