"""
AI Confidence Engine
Version 3.0
"""

from learning.learning_engine import LearningEngine


class ConfidenceEngine:

    def __init__(self):

        self.learning = LearningEngine()

    def calculate(

        self,

        market_score,

        risk,

    ):

        stats = self.learning.analyze()

        confidence = 50

        # -------------------------
        # Win Rate
        # -------------------------

        confidence += (stats["win_rate"] - 50) * 0.10

        # -------------------------
        # Profit Factor
        # -------------------------

        confidence += min(

            stats["profit_factor"],

            3,

        ) * 2

        # -------------------------
        # Experience
        # -------------------------

        exp = stats["experience"]

        if exp >= 100:

            confidence += 20

        elif exp >= 50:

            confidence += 15

        elif exp >= 20:

            confidence += 10

        elif exp >= 10:

            confidence += 5

        elif exp >= 5:

            confidence += 2

        # -------------------------
        # Market Score
        # -------------------------

        confidence += (market_score - 50) * 0.50

        # -------------------------
        # Risk
        # -------------------------

        if risk == "LOW":

            confidence += 5

        elif risk == "HIGH":

            confidence -= 10

        confidence = max(

            30,

            min(

                95,

                round(confidence),

            ),

        )

        return confidence