from providers.base_provider import BaseProvider


class MockStockProvider(BaseProvider):

    def get_data(self):

        return {

            "index": {

                "value": 2945000,

                "change": 0.82,

            },

            "equal_weight": {

                "value": 915000,

                "change": 0.34,

            },

            "real_money": {

                "value": 1850,

            },

            "trade_value": {

                "value": 18200,

            },

            "buy_queue": 184,

            "sell_queue": 72,

            "symbols": [

                {

                    "symbol": "FOLD",

                    "name": "Foolad",

                    "price": 3240,

                    "change": 2.31,

                    "volume": 925000000,

                },

                {

                    "symbol": "FMELI",

                    "name": "Felezi",

                    "price": 7360,

                    "change": 1.87,

                    "volume": 711000000,

                },

                {

                    "symbol": "WEBMELAT",

                    "name": "Bank",

                    "price": 2680,

                    "change": 1.22,

                    "volume": 415000000,

                },

                {

                    "symbol": "SHASTA",

                    "name": "Shasta",

                    "price": 1845,

                    "change": -0.42,

                    "volume": 302000000,

                },

                {

                    "symbol": "AHROM",

                    "name": "ETF",

                    "price": 27150,

                    "change": 3.12,

                    "volume": 91000000,

                },

            ],

        }