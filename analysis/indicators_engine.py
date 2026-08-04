"""
Indicators Engine
Version 1.0
"""

import pandas as pd
import ta


class IndicatorsEngine:

    def calculate(self, df):

        df = df.copy()

        # ==========================
        # Trend
        # ==========================

        df["EMA20"] = ta.trend.ema_indicator(
            df["close"],
            window=20,
        )

        df["EMA50"] = ta.trend.ema_indicator(
            df["close"],
            window=50,
        )

        df["EMA200"] = ta.trend.ema_indicator(
            df["close"],
            window=200,
        )

        # ==========================
        # Momentum
        # ==========================

        df["RSI"] = ta.momentum.rsi(
            df["close"],
            window=14,
        )

        df["MFI"] = ta.volume.money_flow_index(
            high=df["high"],
            low=df["low"],
            close=df["close"],
            volume=df["volume"],
            window=14,
        )

        # ==========================
        # Volatility
        # ==========================

        df["ATR"] = ta.volatility.average_true_range(
            high=df["high"],
            low=df["low"],
            close=df["close"],
            window=14,
        )

        # ==========================
        # MACD
        # ==========================

        macd = ta.trend.MACD(df["close"])

        df["MACD"] = macd.macd()

        df["MACD_SIGNAL"] = macd.macd_signal()

        # ==========================
        # Bollinger
        # ==========================

        bb = ta.volatility.BollingerBands(df["close"])

        df["BB_HIGH"] = bb.bollinger_hband()

        df["BB_LOW"] = bb.bollinger_lband()

        # ==========================
        # ADX
        # ==========================

        df["ADX"] = ta.trend.adx(
            df["high"],
            df["low"],
            df["close"],
        )

        # ==========================
        # OBV
        # ==========================

        df["OBV"] = ta.volume.on_balance_volume(
            df["close"],
            df["volume"],
        )

        # ==========================
        # آخرین وضعیت بازار
        # ==========================

        latest = df.iloc[-1]

        return {

            "RSI": round(latest["RSI"],2),

            "MFI": round(latest["MFI"],2),

            "EMA20": round(latest["EMA20"],2),

            "EMA50": round(latest["EMA50"],2),

            "EMA200": round(latest["EMA200"],2),

            "ATR": round(latest["ATR"],2),

            "MACD": round(latest["MACD"],4),

            "MACD_SIGNAL": round(latest["MACD_SIGNAL"],4),

            "ADX": round(latest["ADX"],2),

            "OBV": round(latest["OBV"],2),

        }