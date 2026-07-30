"""
Experience Engine
Version 1.0
"""

from memory.memory_database import load_memory


class ExperienceEngine:

    def __init__(self):

        self.rows = load_memory()

    def best_asset(self):

        score = {}

        for row in self.rows:

            asset = row["asset"]

            score.setdefault(asset, 0)

            score[asset] += row["pnl"]

        if not score:

            return None

        return max(score, key=score.get)

    def best_market(self):

        score = {}

        for row in self.rows:

            market = row["market"]

            score.setdefault(market, 0)

            score[market] += row["pnl"]

        if not score:

            return None

        return max(score, key=score.get)

    def best_signal(self):

        score = {}

        for row in self.rows:

            signal = row["signal"]

            score.setdefault(signal, 0)

            score[signal] += row["pnl"]

        if not score:

            return None

        return max(score, key=score.get)

    def summary(self):

        return {

            "asset": self.best_asset(),

            "market": self.best_market(),

            "signal": self.best_signal(),

        }