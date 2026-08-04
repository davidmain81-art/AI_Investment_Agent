"""
Market Service
Version 2.0
"""

from data.crypto import get_crypto_prices
from providers.binance_candle_provider import BinanceCandleProvider

from logs.data_logger import save_market_data

from analysis.market_analysis import analyze_market
from analysis.market_score import calculate_market_score


class MarketService:

    def load(self):

        # قیمت لحظه‌ای
        prices = get_crypto_prices()

        save_market_data(prices)

        # کندل‌های واقعی
        df = BinanceCandleProvider().load()

        # تحلیل بازار
        signal, risk = analyze_market(
            prices,
            df,
        )

        market_score = calculate_market_score(
            prices,
            df,
        )

        return {

            "prices": prices,

            "btc_price": prices["BTC"]["price"],

            "signal": signal,

            "risk": risk,

            "market_score": market_score,

            "df": df,

        }