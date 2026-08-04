import sqlite3

from pathlib import Path


DB_PATH = Path("database/feature_store.db")


class PatternStore:


    def __init__(self):

        self.conn = sqlite3.connect(DB_PATH)


    def load_patterns(self):

        cursor = self.conn.cursor()


        cursor.execute(
            """
            SELECT

                asset,
                signal,
                pnl,
                rsi,
                macd,
                ema20,
                ema50,
                trend

            FROM feature_store

            """
        )


        rows = cursor.fetchall()


        patterns = []


        for row in rows:


            pattern = {


                "features": {

                    "rsi": row[3],

                    "macd": row[4],

                    "ema20": row[5],

                    "ema50": row[6],

                    "trend": row[7],

                },


                "decision": row[1],


                "profit_loss": row[2],


                "asset": row[0],


            }


            patterns.append(pattern)


        return patterns



    def close(self):

        self.conn.close()