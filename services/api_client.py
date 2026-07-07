import requests


class APIClient:

    @staticmethod
    def get(url, params=None):

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        return response.json()