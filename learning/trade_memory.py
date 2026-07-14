"""
Trade Memory
Version 1.0
"""

import sqlite3

DATABASE = "investment_agent.db"


class TradeMemory:

    def __init__(self):

        self.connection = sqlite3.connect(DATABASE)

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

    def remember(

        self,

        trade,

        market_score,

        risk,

    ):

        self.cursor.execute(

            """

            INSERT INTO ai_memory(

                asset,

                signal,

                confidence,

                market_score,

                risk,

                pnl,

                result

            )

            VALUES(?,?,?,?,?,?,?)

            """,

            (

                trade["asset"],

                trade["signal"],

                trade["confidence"],

                market_score,

                risk,

                trade["pnl"],

                "WIN" if trade["pnl"] > 0 else "LOSS",

            ),

        )

        self.connection.commit()