"""
Binance Candle Provider
Version 1.1
"""

import requests
import pandas as pd


class BinanceCandleProvider:

    BASE_URL = "https://api.binance.com/api/v3/klines"


    def get_candles(
        self,
        symbol="BTCUSDT",
        interval="1h",
        limit=250,
    ):

        params = {

            "symbol": symbol,

            "interval": interval,

            "limit": limit,

        }


        response = requests.get(

            self.BASE_URL,

            params=params,

            timeout=10,

        )


        response.raise_for_status()


        data = response.json()


        df = pd.DataFrame(

            data,

            columns=[

                "open_time",

                "open",

                "high",

                "low",

                "close",

                "volume",

                "close_time",

                "quote_volume",

                "trades",

                "tb_base",

                "tb_quote",

                "ignore",

            ],

        )


        df["open"] = df["open"].astype(float)

        df["high"] = df["high"].astype(float)

        df["low"] = df["low"].astype(float)

        df["close"] = df["close"].astype(float)

        df["volume"] = df["volume"].astype(float)


        return df[

            [

                "open",

                "high",

                "low",

                "close",

                "volume",

            ]

        ]



    # ==========================================
    # Compatibility Loader
    # Used by Market Engine
    # ==========================================

    def load(
        self,
        symbol="BTCUSDT",
        interval="1h",
        limit=250,
    ):

        return self.get_candles(

            symbol=symbol,

            interval=interval,

            limit=limit,

        )