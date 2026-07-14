"""
Market Service
Version 1.0
"""

from logs.data_logger import save_market_data

from data.crypto import get_crypto_prices

from analysis.market_analysis import analyze_market
from analysis.market_score import calculate_market_score


class MarketService:

    def load(self):

        prices = get_crypto_prices()

        save_market_data(prices)

        signal, risk = analyze_market(prices)

        score = calculate_market_score(prices)

        return {

            "prices": prices,

            "signal": signal,

            "risk": risk,

            "market_score": score,

            "btc_price": prices["BTC"]["price"]

        }