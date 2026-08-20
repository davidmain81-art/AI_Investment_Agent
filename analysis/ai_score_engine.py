"""
AI Score Engine
Version 4.0
Sample-Adjusted Pattern Learning
"""


class AIScoreEngine:

    def calculate(
        self,
        market_score,
        learning,
        confidence,
        risk,
        optimizer_score=0,
        pattern_score=0,
    ):

        # ==========================================
        # Experience / Sample Size
        # ==========================================

        experience = learning.get(
            "experience",
            0,
        )

        sample_factor = min(
            experience / 50.0,
            1.0,
        )

        # ==========================================
        # Base Market Score
        # ==========================================

        score = float(market_score)

        # ==========================================
        # Confidence
        # ==========================================

        confidence_effect = (
            confidence - 50
        ) * 0.20

        score += confidence_effect

        # ==========================================
        # Learning - Sample Adjusted
        # ==========================================

        win_rate = learning.get(
            "win_rate",
            50,
        )

        learning_effect = (
            (win_rate - 50)
            * 0.10
            * sample_factor
        )

        score += learning_effect

        # ==========================================
        # Profit Factor - Sample Adjusted
        # ==========================================

        profit_factor = learning.get(
            "profit_factor",
            1,
        )

        if profit_factor > 1:

            profit_factor_effect = min(
                (profit_factor - 1) * 2,
                5,
            )

        else:

            profit_factor_effect = 0

        profit_factor_effect *= sample_factor

        score += profit_factor_effect

        # ==========================================
        # Pattern Recognition - Sample Adjusted
        # ==========================================

        pattern_effect = (
            pattern_score
            * 0.10
            * sample_factor
        )

        score += pattern_effect

        # ==========================================
        # Risk Adjustment
        # ==========================================

        if risk == "LOW":

            score += 5

        elif risk == "MEDIUM":

            score += 0

        elif risk == "HIGH":

            score -= 10

        # ==========================================
        # Optimizer - Sample Adjusted
        # ==========================================

        raw_optimizer_score = optimizer_score

        optimizer_score = max(
            -20,
            min(
                20,
                optimizer_score,
            ),
        )

        optimizer_effect = (
            optimizer_score
            * sample_factor
        )

        score += optimizer_effect

        # ==========================================
        # Final Clamp
        # ==========================================

        score = max(
            0,
            min(
                100,
                round(score, 2),
            ),
        )

        # ==========================================
        # Debug
        # ==========================================

        print("=" * 60)

        print("AI SCORE DEBUG")

        print(
            "Market Score       :",
            market_score,
        )

        print(
            "Confidence         :",
            confidence,
        )

        print(
            "Confidence Effect  :",
            round(
                confidence_effect,
                2,
            ),
        )

        print(
            "Experience         :",
            experience,
        )

        print(
            "Sample Factor      :",
            round(
                sample_factor,
                2,
            ),
        )

        print(
            "Learning Effect    :",
            round(
                learning_effect,
                2,
            ),
        )

        print(
            "Profit Factor      :",
            profit_factor,
        )

        print(
            "PF Effect          :",
            round(
                profit_factor_effect,
                2,
            ),
        )

        print(
            "Pattern Score      :",
            pattern_score,
        )

        print(
            "Pattern Effect     :",
            round(
                pattern_effect,
                2,
            ),
        )

        print(
            "Optimizer Raw      :",
            raw_optimizer_score,
        )

        print(
            "Optimizer Effect   :",
            round(
                optimizer_effect,
                2,
            ),
        )

        print(
            "Risk                :",
            risk,
        )

        print(
            "FINAL AI SCORE     :",
            score,
        )

        print("=" * 60)

        return score