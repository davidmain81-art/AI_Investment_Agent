from providers.base_provider import BaseProvider


class MockCryptoProvider(BaseProvider):

    def get_data(self):

        return {

            "BTC": {
                "price": 64518,
                "change": -0.28,
            },

            "ETH": {
                "price": 1926,
                "change": 0.73,
            },

            "BNB": {
                "price": 569,
                "change": -0.64,
            },

            "SOL": {
                "price": 75,
                "change": -0.24,
            },

            "XRP": {
                "price": 1.09,
                "change": -1.38,
            },

        }