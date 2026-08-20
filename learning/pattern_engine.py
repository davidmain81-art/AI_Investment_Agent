"""
Pattern Recognition Engine
Version 1.3
Context Aware Pattern Learning
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
                "total": 0,
                "wins": 0,
                "losses": 0,
                "win_rate": 0,
            }

        wins = len(
            df[df.result == "WIN"]
        )

        losses = len(
            df[df.result == "LOSS"]
        )

        return {

            "total": len(df),

            "wins": wins,

            "losses": losses,

            "win_rate": round(
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

        if len(pattern) == 0:

            return {

                "pattern":
                f"RSI < {threshold}",

                "trades": 0,

                "wins": 0,

                "win_rate": 0

            }

        wins = len(
            pattern[
                pattern.result == "WIN"
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

        if len(pattern) == 0:

            return {

                "pattern":
                "EMA20 > EMA50",

                "trades": 0,

                "wins": 0,

                "win_rate": 0

            }

        wins = len(
            pattern[
                pattern.result == "WIN"
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
                wins / len(pattern) * 100,
                2
            )

        }

    # ==========================
    # Pattern Score Generator
    # ==========================

    def analyze(
        self,
        current_rsi=None,
        current_ema20=None,
        current_ema50=None,
    ):

        rsi_pattern = self.analyze_rsi()

        ema_pattern = self.analyze_ema_trend()

        scores = []

        # ==========================================
        # Sample Size Confidence
        # 20 trades = full confidence
        # ==========================================

        def adjusted_score(pattern):

            trades = pattern.get(
                "trades",
                0
            )

            win_rate = pattern.get(
                "win_rate",
                0
            )

            if trades <= 0:
                return None

            sample_factor = min(
                trades / 20.0,
                1.0
            )

            effective_score = (
                win_rate * sample_factor
            )

            return effective_score

        # ==========================================
        # RSI Pattern Context
        # ==========================================

        rsi_score = adjusted_score(
            rsi_pattern
        )

        if rsi_score is not None:

            # اگر وضعیت فعلی بازار با الگوی تاریخی
            # مطابقت ندارد، این Pattern نباید امتیاز بدهد.

            if current_rsi is not None:

                current_rsi_matches = (
                    current_rsi < 40
                )

                if not current_rsi_matches:

                    rsi_score = 0

            scores.append(
                rsi_score
            )

        # ==========================================
        # EMA Pattern Context
        # ==========================================

        ema_score = adjusted_score(
            ema_pattern
        )

        if ema_score is not None:

            if (
                current_ema20 is not None
                and current_ema50 is not None
            ):

                current_ema_matches = (
                    current_ema20 >
                    current_ema50
                )

                if not current_ema_matches:

                    ema_score = 0

            scores.append(
                ema_score
            )

        # ==========================================
        # Final Pattern Score
        # ==========================================

        if len(scores) == 0:

            pattern_score = 0

        else:

            pattern_score = round(
                sum(scores) / len(scores),
                2
            )

        return {

            "pattern_score":
            pattern_score,

            "patterns": {

                "RSI":
                rsi_pattern,

                "EMA":
                ema_pattern

            }

        }

    # ==========================
    # Full Report
    # ==========================

    def report(self):

        print("=" * 50)

        print(
            "PATTERN ANALYSIS"
        )

        print("=" * 50)

        print(
            self.statistics()
        )

        print()

        print(
            self.analyze()
        )

    # ==========================
    # Close Database
    # ==========================

    def close(self):

        self.conn.close()