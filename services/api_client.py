import requests


class APIClient:

    @staticmethod
    def get(url, params=None):

        try:

            response = requests.get(
                url,
                params=params,
                timeout=10,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.Timeout:

            print("\n❌ Connection timed out.")
            print("CoinGecko API did not respond.\n")

            return None

        except requests.exceptions.RequestException as e:

            print(f"\n❌ API Error: {e}\n")

            return None