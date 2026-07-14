"""
AI Confidence Engine
Version 1.0
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

        # Historical Performance
        confidence += (stats["confidence"] - 50) * 0.40

        # Market Score
        confidence += (market_score - 50) * 0.50

        # Risk
        if risk == "LOW":

            confidence += 10

        elif risk == "HIGH":

            confidence -= 15

        confidence = round(confidence)

        confidence = max(0, min(99, confidence))

        return confidence