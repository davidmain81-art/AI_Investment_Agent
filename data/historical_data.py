"""
Historical Data Loader
Version 1.0
"""

from providers.binance_candle_provider import BinanceCandleProvider


class HistoricalDataLoader:

    def __init__(self, provider=None):

        self.provider = provider or BinanceCandleProvider()

    # ==========================================
    # Load Historical Candles
    # ==========================================

    def load(
        self,
        symbol="BTCUSDT",
        interval="1h",
        limit=250,
        start_time=None,
        end_time=None,
        include_timestamps=True,
    ):

        return self.provider.get_candles(
            symbol=symbol,
            interval=interval,
            limit=limit,
            start_time=start_time,
            end_time=end_time,
            include_timestamps=include_timestamps,
        )