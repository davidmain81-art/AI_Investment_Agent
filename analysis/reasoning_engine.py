"""
AI Reasoning Engine
Version 1.0
"""


class ReasoningEngine:

    def build(

        self,

        signal,

        risk,

        market_score,

        confidence,

        ai_stats,

    ):

        reasons = []

        # ===========================
        # Signal
        # ===========================

        if signal == "BUY":

            reasons.append(
                "Trend is bullish."
            )

        elif signal == "SELL":

            reasons.append(
                "Trend is bearish."
            )

        else:

            reasons.append(
                "Market is neutral."
            )

        # ===========================
        # Risk
        # ===========================

        if risk == "LOW":

            reasons.append(
                "Risk level is LOW."
            )

        elif risk == "MEDIUM":

            reasons.append(
                "Risk level is MEDIUM."
            )

        else:

            reasons.append(
                "Risk level is HIGH."
            )

        # ===========================
        # Market Score
        # ===========================

        reasons.append(

            f"Market Score = {market_score}/100"

        )

        # ===========================
        # AI Experience
        # ===========================

        reasons.append(

            f"Historical Win Rate = {ai_stats['confidence']}%"

        )

        reasons.append(

            f"Experience = {ai_stats['experience']} trades"

        )

        # ===========================
        # Final Confidence
        # ===========================

        reasons.append(

            f"Final Confidence = {confidence}%"

        )

        return reasons