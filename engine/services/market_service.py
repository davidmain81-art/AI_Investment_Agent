"""
Market Service
Version 1.1
"""

import pandas as pd

from logs.data_logger import save_market_data
from data.crypto import get_crypto_prices

from analysis.market_analysis import analyze_market
from analysis.market_score import calculate_market_score


class MarketService:

    def load(self):

        prices = get_crypto_prices()

        save_market_data(prices)

        # ---------------------------------
        # Temporary OHLC dataframe
        # (در نسخه بعد با Binance Candle Provider جایگزین می‌شود)
        # ---------------------------------

        btc = prices["BTC"]["price"]

        df = pd.DataFrame({

            "open": [btc] * 250,
            "high": [btc] * 250,
            "low": [btc] * 250,
            "close": [btc] * 250,
            "volume": [1000] * 250,

        })

        signal, risk, market_score, indicators = analyze_market(
            prices,
            df,
        )

        score = calculate_market_score(prices)

        return {

            "prices": prices,

            "signal": signal,

            "risk": risk,

            "market_score": market_score,

            "indicators": indicators,

            "btc_price": prices["BTC"]["price"],

        }