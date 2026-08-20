"""
Market Service
Version 2.1
"""

from data.crypto import get_crypto_prices
from providers.binance_candle_provider import BinanceCandleProvider

from logs.data_logger import save_market_data

from analysis.market_analysis import analyze_market
from analysis.market_score import calculate_market_score


class MarketService:

    def load(self):

        # ==========================================
        # Crypto Prices
        # ==========================================

        prices = get_crypto_prices()

        save_market_data(prices)

        # ==========================================
        # Binance Candles
        # ==========================================

        df = BinanceCandleProvider().load()

        # ==========================================
        # Market Analysis
        # ==========================================

        signal, risk, analysis_score, indicators = analyze_market(
            prices,
            df,
        )

        # ==========================================
        # Market Score
        # ==========================================

        market_score = calculate_market_score(
            prices,
        )

        # ==========================================
        # Result
        # ==========================================

        return {

            "prices": prices,

            "btc_price": prices["BTC"]["price"],

            "signal": signal,

            "risk": risk,

            "market_score": market_score,

            "analysis_score": analysis_score,

            "indicators": indicators,

            "df": df,

        }