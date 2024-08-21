import requests
from config.settings import BASE_URL


class CatFactsAPIClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def get_facts(self, params=None):
        """
        Retrieves a list of cat facts, optionally with query parameters.
        """
        url = f"{self.base_url}/facts"
        response = requests.get(url, params=params)
        return response

    def get_fact_by_id(self, fact_id):
        """
        Retrieves a specific fact by `_id`.
        """
        url = f"{self.base_url}/facts/{fact_id}"
        response = requests.get(url)
        return response
