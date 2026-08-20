"""
Paper Trading
Version 2.0

Paper Trading is responsible for recording
CLOSED simulated trades and calculating real PnL.

Trade Lifecycle is responsible for deciding
when a trade is closed.
"""

import sqlite3

from datetime import datetime

from data.feature_store import FeatureStore
from memory.memory_engine import MemoryEngine


DB = "database/investment_agent.db"


class PaperTrading:

    def execute(self, order):

        """
        Execute / record a paper trade.

        Important:
        - No random PnL.
        - If exit price is missing, trade remains OPEN.
        - PnL is calculated only when an exit price exists.
        """

        if order is None:
            return None

        # ==========================================
        # Basic Data
        # ==========================================

        asset = order.get("asset", "UNKNOWN")

        signal = order.get("signal", "HOLD")

        entry = float(
            order.get("entry", 0)
        )

        exit_price = order.get("exit")

        stop_loss = float(
            order.get("stop_loss", 0)
        )

        take_profit = float(
            order.get("take_profit", 0)
        )

        quantity = float(
            order.get("quantity", 1.0)
        )

        # ==========================================
        # Validate Entry
        # ==========================================

        if entry <= 0:

            print("PAPER TRADE REJECTED: INVALID ENTRY")

            return None

        if quantity <= 0:

            print("PAPER TRADE REJECTED: INVALID QUANTITY")

            return None

        # ==========================================
        # OPEN TRADE
        # ==========================================

        if exit_price is None:

            print("=" * 60)
            print("PAPER TRADE OPEN")
            print("Asset       :", asset)
            print("Signal      :", signal)
            print("Entry       :", entry)
            print("Stop Loss   :", stop_loss)
            print("Take Profit :", take_profit)
            print("Quantity    :", quantity)
            print("=" * 60)

            return {
                "status": "OPEN",
                "asset": asset,
                "signal": signal,
                "entry_price": entry,
                "exit_price": None,
                "quantity": quantity,
                "pnl": 0,
            }

        # ==========================================
        # CLOSED TRADE
        # ==========================================

        exit_price = float(exit_price)

        # ==========================================
        # Calculate Real PnL
        # ==========================================

        if "SELL" in signal:

            gross_pnl = (
                entry - exit_price
            ) * quantity

        else:

            gross_pnl = (
                exit_price - entry
            ) * quantity

        gross_pnl = round(
            gross_pnl,
            2
        )

        # ==========================================
        # Result
        # ==========================================

        if gross_pnl > 0:

            result = "WIN"

        elif gross_pnl < 0:

            result = "LOSS"

        else:

            result = "BREAKEVEN"

        # ==========================================
        # Paper Trade Database
        # ==========================================

        conn = sqlite3.connect(DB)

        cur = conn.cursor()

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS paper_trades(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

                asset TEXT,

                signal TEXT,

                entry REAL,

                exit REAL,

                stop_loss REAL,

                take_profit REAL,

                quantity REAL,

                pnl REAL,

                result TEXT

            )
            """
        )

        # ==========================================
        # Compatibility Migration
        # ==========================================

        columns = [
            row[1]
            for row in cur.execute(
                "PRAGMA table_info(paper_trades)"
            ).fetchall()
        ]

        if "exit" not in columns:

            try:

                cur.execute(
                    "ALTER TABLE paper_trades ADD COLUMN exit REAL"
                )

            except sqlite3.OperationalError:

                pass

        if "quantity" not in columns:

            try:

                cur.execute(
                    "ALTER TABLE paper_trades ADD COLUMN quantity REAL"
                )

            except sqlite3.OperationalError:

                pass

        # ==========================================
        # Save Paper Trade
        # ==========================================

        cur.execute(
            """
            INSERT INTO paper_trades(

                asset,
                signal,
                entry,
                exit,
                stop_loss,
                take_profit,
                quantity,
                pnl,
                result

            )

            VALUES(?,?,?,?,?,?,?,?,?)

            """,
            (
                asset,
                signal,
                entry,
                exit_price,
                stop_loss,
                take_profit,
                quantity,
                gross_pnl,
                result,
            )
        )

        conn.commit()

        conn.close()

        # ==========================================
        # Feature Store
        # ==========================================

        store = FeatureStore()

        store.save({

            "timestamp": datetime.now().isoformat(),

            "asset": asset,

            "signal": signal,

            "entry": entry,

            "exit": exit_price,

            "pnl": gross_pnl,

            "result": result,

            "ai_score": order.get(
                "ai_score",
                0
            ),

            "confidence": order.get(
                "confidence",
                0
            ),

            "risk": order.get(
                "risk",
                ""
            ),

            "market_score": order.get(
                "market_score",
                0
            ),

            "learning": (
                order.get("learning", {}).get(
                    "win_rate",
                    0
                )
                if isinstance(
                    order.get("learning", 0),
                    dict
                )
                else order.get(
                    "learning",
                    0
                )
            ),

            "optimizer": order.get(
                "optimizer",
                0
            ),

            "position_size": order.get(
                "position_size",
                0
            ),

            "stop_loss": stop_loss,

            "take_profit": take_profit,

            # ======================================
            # Indicators
            # ======================================

            "rsi": order.get("rsi"),

            "mfi": order.get("mfi"),

            "macd": order.get("macd"),

            "ema20": order.get("ema20"),

            "ema50": order.get("ema50"),

            "ema200": order.get("ema200"),

            "atr": order.get("atr"),

            "adx": order.get("adx"),

            "obv": order.get("obv"),

            "vwap": order.get("vwap"),

            "volume": order.get("volume"),

            "spread": order.get("spread"),

            "volatility": order.get("volatility"),

            "funding_rate": order.get(
                "funding_rate"
            ),

            "open_interest": order.get(
                "open_interest"
            ),

            "fear_greed": order.get(
                "fear_greed"
            ),

            "news_score": order.get(
                "news_score"
            ),

        })

        store.close()

        # ==========================================
        # Memory Engine
        # ==========================================

        memory = MemoryEngine()

        memory.remember_trade({

            "asset": asset,

            "signal": signal,

            "entry_price": entry,

            "exit_price": exit_price,

            "quantity": quantity,

            "gross_pnl": gross_pnl,

            "pnl": gross_pnl,

            "market": "CRYPTO",

        })

        # ==========================================
        # Result
        # ==========================================

        print("=" * 60)
        print("PAPER TRADE CLOSED")
        print("Asset       :", asset)
        print("Signal      :", signal)
        print("Entry       :", entry)
        print("Exit        :", exit_price)
        print("Quantity    :", quantity)
        print("Gross PnL   :", gross_pnl)
        print("Result      :", result)
        print("=" * 60)

        return {

            "status": "CLOSED",

            "asset": asset,

            "signal": signal,

            "entry_price": entry,

            "exit_price": exit_price,

            "quantity": quantity,

            "gross_pnl": gross_pnl,

            "pnl": gross_pnl,

            "result": result,

        }