"""
AI Confidence Engine
Version 0.9.2
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

        # Historical Accuracy

        confidence += (stats["confidence"] - 50) * 0.40

        # Market Score

        confidence += (market_score - 50) * 0.50

        # Risk Adjustment

        if risk == "LOW":

            confidence += 10

        elif risk == "MEDIUM":

            confidence += 0

        else:

            confidence -= 15

        confidence = round(confidence)

        confidence = max(0, min(99, confidence))

        return confidence