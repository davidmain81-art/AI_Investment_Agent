"""
AI Confidence Engine
Version 2.2
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
        # Sample Size Confidence
        # -------------------------

        exp = stats["experience"]

        sample_factor = min(
            exp / 20.0,
            1.0
        )

        # -------------------------
        # Learning Factors
        # -------------------------

        learning_adjustment = 0

        # -------------------------
        # Win Rate
        # -------------------------

        learning_adjustment += (
            stats["win_rate"] - 50
        ) * 0.10

        # -------------------------
        # Profit Factor
        # -------------------------

        if stats["profit_factor"] == 0:

            learning_adjustment -= 10

        elif stats["profit_factor"] > 1:

            learning_adjustment += min(
                stats["profit_factor"],
                3,
            ) * 2

        # -------------------------
        # Apply Sample Factor
        # -------------------------

        learning_adjustment *= sample_factor

        confidence += learning_adjustment

        # -------------------------
        # Experience
        # -------------------------

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

        confidence += (
            market_score - 50
        ) * 0.50

        # -------------------------
        # Risk
        # -------------------------

        if risk == "LOW":

            confidence += 5

        elif risk == "HIGH":

            confidence -= 10

        # -------------------------
        # Final Clamp
        # -------------------------

        confidence = max(

            30,

            min(

                95,

                round(confidence),

            ),

        )

        return confidence