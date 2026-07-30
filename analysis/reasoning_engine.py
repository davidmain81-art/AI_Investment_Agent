"""
AI Reasoning Engine
Version 2.0
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

            reasons.append("Trend is bullish.")

        elif signal == "SELL":

            reasons.append("Trend is bearish.")

        else:

            reasons.append("Market is neutral.")

        # ===========================
        # Risk
        # ===========================

        reasons.append(f"Risk level is {risk}.")

        # ===========================
        # Market
        # ===========================

        reasons.append(f"Market Score = {market_score}/100")

        # ===========================
        # Learning
        # ===========================

        reasons.append(

            f"Historical Win Rate = {ai_stats['win_rate']}%"

        )

        reasons.append(

            f"Experience = {ai_stats['experience']} trades"

        )

        reasons.append(

            f"Profit Factor = {ai_stats['profit_factor']}"

        )

        reasons.append(

            f"Best Asset = {ai_stats['best_asset']}"

        )

        reasons.append(

            f"Best Signal = {ai_stats['best_signal']}"

        )

        # ===========================
        # Confidence
        # ===========================

        reasons.append(

            f"Final Confidence = {confidence}%"

        )

        # ===========================
        # Final Conclusion
        # ===========================

        if signal == "BUY":

            reasons.append(

                "AI recommends opening or keeping BUY positions."

            )

        elif signal == "SELL":

            reasons.append(

                "AI recommends avoiding long positions."

            )

        else:

            reasons.append(

                "AI recommends waiting for a better opportunity."

            )

        return reasons