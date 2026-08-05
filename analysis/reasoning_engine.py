"""
AI Reasoning Engine
Version 3.0 Stable
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

        # =====================================
        # Normalize Signal
        # =====================================

        signal = str(signal).upper()

        is_buy = "BUY" in signal
        is_sell = "SELL" in signal

        # =====================================
        # Trend Analysis
        # =====================================

        if is_buy:

            reasons.append("Trend is bullish.")

        elif is_sell:

            reasons.append("Trend is bearish.")

        else:

            reasons.append("Market is neutral.")

        # =====================================
        # Risk
        # =====================================

        reasons.append(
            f"Risk level is {risk}."
        )

        # =====================================
        # Market Score
        # =====================================

        reasons.append(
            f"Market Score = {market_score}/100"
        )

        # =====================================
        # AI Learning
        # =====================================

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

        # =====================================
        # Confidence
        # =====================================

        reasons.append(
            f"Final Confidence = {confidence}%"
        )

        # =====================================
        # Final Recommendation
        # =====================================

        if is_buy:

            reasons.append(
                "AI recommends opening or keeping BUY positions."
            )

        elif is_sell:

            reasons.append(
                "AI recommends avoiding long positions."
            )

        else:

            reasons.append(
                "AI recommends waiting for a better opportunity."
            )

        return reasons