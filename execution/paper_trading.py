import random
import sqlite3

from datetime import datetime

from data.feature_store import FeatureStore
from memory.memory_engine import MemoryEngine


DB = "database/investment_agent.db"


class PaperTrading:

    def execute(self, order):

        """
        Paper Trading Simulation
        """

        result = random.choice([
            "WIN",
            "LOSS",
        ])

        pnl = round(
            random.uniform(-5, 10),
            2
        )


        # ===========================================
        # Paper Trade Database
        # ===========================================

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

                stop_loss REAL,

                take_profit REAL,

                pnl REAL,

                result TEXT

            )
            """
        )


        cur.execute(
            """
            INSERT INTO paper_trades(

                asset,

                signal,

                entry,

                stop_loss,

                take_profit,

                pnl,

                result

            )

            VALUES(?,?,?,?,?,?,?)

            """,
            (

                order["asset"],

                order["signal"],

                order["entry"],

                order["stop_loss"],

                order["take_profit"],

                pnl,

                result,

            )
        )


        conn.commit()
        conn.close()



        # ===========================================
        # Feature Store
        # ===========================================

        store = FeatureStore()


        store.save({

            "timestamp": datetime.now().isoformat(),

            "asset": order["asset"],

            "signal": order["signal"],


            "entry": order["entry"],

            "exit": order.get(
                "exit",
                0
            ),


            "pnl": pnl,

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


            "learning": order.get(
                "learning",
                0
            ),


            "optimizer": order.get(
                "optimizer",
                0
            ),


            "position_size": order.get(
                "position_size",
                0
            ),


            "stop_loss": order["stop_loss"],

            "take_profit": order["take_profit"],



            # Indicators

            "rsi": order.get("rsi", 0),

            "mfi": order.get("mfi", 0),

            "macd": order.get("macd", 0),


            "ema20": order.get("ema20", 0),

            "ema50": order.get("ema50", 0),

            "ema200": order.get("ema200", 0),


            "atr": order.get("atr", 0),

            "adx": order.get("adx", 0),


            "obv": order.get("obv", 0),

            "vwap": order.get("vwap", 0),


            "volume": order.get("volume", 0),

            "spread": order.get("spread", 0),


            "volatility": order.get(
                "volatility",
                0
            ),


            "trend": order.get(
                "trend",
                ""
            ),


            "funding_rate": order.get(
                "funding_rate",
                0
            ),


            "open_interest": order.get(
                "open_interest",
                0
            ),


            "fear_greed": order.get(
                "fear_greed",
                0
            ),


            "news_score": order.get(
                "news_score",
                0
            ),

        })


        store.close()



        # ===========================================
        # Memory Engine
        # ===========================================

        memory = MemoryEngine()


        memory.remember_trade({

            "asset": order["asset"],

            "signal": order["signal"],


            "entry_price": order["entry"],


            "exit_price": order.get(
                "exit",
                order["entry"]
            ),


            "gross_pnl": pnl,


            "pnl": pnl,


            "market": "CRYPTO",

        })



        return {

            "result": result,

            "pnl": pnl,

        }