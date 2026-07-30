import requests

from data.market_cache import MarketCache


class BinanceProvider:

    BASE_URL = "https://api.binance.com/api/v3/ticker/24hr"


    def __init__(self):

        self.cache = MarketCache()



    def get_price(self, symbol):

        params = {
            "symbol": symbol
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=10
        )

        data = response.json()

        return {
            "price": float(data["lastPrice"]),
            "change": float(data["priceChangePercent"])
        }



    def get_data(self):

        # اگر داده تازه داریم، از Cache بخوان

        if self.cache.is_valid(30):

            return self.cache.get()



        symbols = [
            "BTCUSDT",
            "ETHUSDT",
            "BNBUSDT",
            "SOLUSDT",
            "XRPUSDT",
        ]


        result = {}


        for symbol in symbols:

            try:

                item = self.get_price(symbol)

                name = symbol.replace(
                    "USDT",
                    ""
                )

                result[name] = item


            except Exception as e:

                print(
                    "Binance Error:",
                    symbol,
                    e
                )


        # ذخیره آخرین داده موفق

        if result:

            self.cache.set(result)


        return result