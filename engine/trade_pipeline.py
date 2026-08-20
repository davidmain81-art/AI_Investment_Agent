"""
Trade Pipeline
Version 1.2

Closed trades are processed through:

TradePipeline
    ↓
FeatureStore
    ↓
MemoryEngine
"""

import sqlite3
from database.database import get_connection

from data.feature_store import FeatureStore
from memory.memory_engine import MemoryEngine


class TradePipeline:

    def __init__(self):

        self.memory = MemoryEngine()
        self.feature_store = FeatureStore()

    def process(self, trade):

        if trade is None:
            return

        if trade.get("status") != "CLOSED":
            return

        # ==========================================
        # Get Trade ID
        # ==========================================

        trade_id = trade.get("id")

        if trade_id is not None:

            # ======================================
            # Load Entry Features
            # ======================================

            connection = get_connection()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT *
                FROM trade_features
                WHERE trade_id=?
                """,
                (trade_id,),
            )

            feature_row = cursor.fetchone()

            connection.close()

            # ======================================
            # Feature Found
            # ======================================

            if feature_row:

                features = dict(feature_row)

                feature_data = {

                    "timestamp": features.get(
                        "created_at"
                    ),

                    "asset": features.get(
                        "asset",
                        trade.get("asset"),
                    ),

                    "signal": features.get(
                        "signal",
                        trade.get("signal"),
                    ),

                    "entry": features.get(
                        "entry",
                        trade.get("entry_price"),
                    ),

                    "exit": trade.get(
                        "exit_price"
                    ),

                    "pnl": trade.get(
                        "pnl"
                    ),

                    "result": trade.get(
                        "result"
                    ),

                    "ai_score": features.get(
                        "ai_score"
                    ),

                    "confidence": features.get(
                        "confidence"
                    ),

                    "risk": features.get(
                        "risk"
                    ),

                    "market_score": features.get(
                        "market_score"
                    ),

                    "learning": features.get(
                        "learning"
                    ),

                    "optimizer": features.get(
                        "optimizer"
                    ),

                    "position_size": features.get(
                        "position_size"
                    ),

                    "stop_loss": features.get(
                        "stop_loss"
                    ),

                    "take_profit": features.get(
                        "take_profit"
                    ),

                    "rsi": features.get(
                        "rsi"
                    ),

                    "mfi": features.get(
                        "mfi"
                    ),

                    "macd": features.get(
                        "macd"
                    ),

                    "macd_signal": features.get(
                        "macd_signal"
                    ),

                    "pattern_score": features.get(
                        "pattern_score"
                    ),

                    "ema20": features.get(
                        "ema20"
                    ),

                    "ema50": features.get(
                        "ema50"
                    ),

                    "ema200": features.get(
                        "ema200"
                    ),

                    "atr": features.get(
                        "atr"
                    ),

                    "adx": features.get(
                        "adx"
                    ),

                    "obv": features.get(
                        "obv"
                    ),

                    "vwap": None,

                    "volume": None,

                    "spread": None,

                    "volatility": None,

                    "trend": None,

                    "funding_rate": None,

                    "open_interest": None,

                    "fear_greed": None,

                    "news_score": None,

                }

                self.feature_store.save(
                    feature_data
                )

                print(
                    "FEATURE STORE: TRADE SAVED",
                    trade_id,
                )

            else:

                print(
                    "FEATURE STORE: ENTRY FEATURES NOT FOUND",
                    trade_id,
                )

        # ==========================================
        # Memory
        # ==========================================

        self.memory.remember_trade(trade)