"""
Market Service
Version 2.2
"""

from logs.data_logger import save_market_data
from data.crypto import get_crypto_prices

from providers.binance_candle_provider import BinanceCandleProvider

from analysis.market_analysis import analyze_market
from analysis.market_score import calculate_market_score


class MarketService:

    def load(self):

        # ==========================================
        # Crypto Market Prices
        # ==========================================

        prices = get_crypto_prices()

        save_market_data(prices)

        # ==========================================
        # Real Binance OHLC Data
        # ==========================================

        df = BinanceCandleProvider().load()

        # ==========================================
        # Technical Market Analysis
        # ==========================================

        (
            signal,
            risk,
            technical_score,
            indicators,
        ) = analyze_market(
            prices,
            df,
        )

        # ==========================================
        # Global Market Score
        # ==========================================

        market_score = calculate_market_score(
            prices,
        )

        # ==========================================
        # Result
        # ==========================================

        return {

            "prices": prices,

            "signal": signal,

            "risk": risk,

            "market_score": market_score,

            "technical_score": technical_score,

            "indicators": indicators,

            "btc_price": prices["BTC"]["price"],

            "df": df,

        }
