"""
Pattern Recognition Engine
Version 1.2
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

                "trades":0,

                "win_rate":0

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

                "trades":0,

                "win_rate":0

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
    # Pattern Score Generator
    # ==========================

    def analyze(self):


        rsi_pattern = self.analyze_rsi()

        ema_pattern = self.analyze_ema_trend()


        scores = []


        if rsi_pattern.get("trades",0) > 0:

            scores.append(
                rsi_pattern.get("win_rate",0)
            )


        if ema_pattern.get("trades",0) > 0:

            scores.append(
                ema_pattern.get("win_rate",0)
            )


        if len(scores)==0:

            pattern_score = 0


        else:

            pattern_score = round(
                sum(scores) / len(scores),
                2
            )


        return {

            "pattern_score": pattern_score,

            "patterns": {

                "RSI": rsi_pattern,

                "EMA": ema_pattern

            }

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