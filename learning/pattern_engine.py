"""
Pattern Recognition Engine
Version 1.1
"""

import sqlite3
import pandas as pd


DB = "database/feature_store.db"


class PatternEngine:


    def __init__(self):

        self.conn = sqlite3.connect(DB)



    # ==========================
    # Load Features
    # ==========================

    def load_features(self):

        query = """

        SELECT *

        FROM feature_store

        """

        return pd.read_sql_query(
            query,
            self.conn
        )



    # ==========================
    # Basic Statistics
    # ==========================

    def statistics(self):

        df = self.load_features()


        if df.empty:

            return {
                "total":0,
                "wins":0,
                "losses":0,
            }


        wins = len(
            df[df.result=="WIN"]
        )


        losses = len(
            df[df.result=="LOSS"]
        )


        return {

            "total":len(df),

            "wins":wins,

            "losses":losses,

            "win_rate":round(
                wins / len(df) * 100,
                2
            )

        }



    # ==========================
    # RSI Pattern
    # ==========================

    def analyze_rsi(
        self,
        threshold=40
    ):


        df = self.load_features()


        pattern = df[
            df["rsi"] < threshold
        ]


        if len(pattern)==0:

            return {

                "pattern":
                f"RSI < {threshold}",

                "trades":0

            }



        wins = len(
            pattern[
                pattern.result=="WIN"
            ]
        )


        return {


            "pattern":
            f"RSI < {threshold}",


            "trades":
            len(pattern),


            "wins":
            wins,


            "win_rate":
            round(
                wins / len(pattern) * 100,
                2
            )

        }



    # ==========================
    # EMA Trend Pattern
    # ==========================

    def analyze_ema_trend(self):


        df = self.load_features()


        pattern = df[
            df["ema20"] >
            df["ema50"]
        ]


        if len(pattern)==0:

            return {

                "pattern":
                "EMA20 > EMA50",

                "trades":0

            }



        wins=len(
            pattern[
                pattern.result=="WIN"
            ]
        )


        return {

            "pattern":
            "EMA20 > EMA50",

            "trades":
            len(pattern),

            "wins":
            wins,

            "win_rate":
            round(
                wins / len(pattern) *100,
                2
            )

        }



    # ==========================
    # Full Report
    # ==========================

    def report(self):


        print("="*50)

        print(
            "PATTERN ANALYSIS"
        )

        print("="*50)


        print(
            self.statistics()
        )


        print()

        print(
            self.analyze_rsi()
        )


        print()

        print(
            self.analyze_ema_trend()
        )



    def close(self):

        self.conn.close()