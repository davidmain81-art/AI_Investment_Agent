"""
AI Optimizer
Version 2.1 Sample Size Aware
"""


class AIOptimizer:

    def optimize(self, learning):

        # ==========================================
        # Learning Statistics
        # ==========================================

        win_rate = learning["win_rate"]
        profit_factor = learning["profit_factor"]
        recovery = learning["recovery_factor"]
        experience = learning["experience"]

        # ==========================================
        # Sample Size Confidence
        # ==========================================
        #
        # Small number of trades must have limited
        # influence on the optimizer.
        #
        # 3 trades  -> 15%
        # 5 trades  -> 25%
        # 10 trades -> 50%
        # 20+       -> 100%
        #

        sample_factor = min(
            experience / 20,
            1.0,
        )

        # ==========================================
        # Raw Performance Score
        # ==========================================

        score = 0

        # ==========================================
        # Win Rate
        # ==========================================

        if win_rate >= 70:

            score += 25

        elif win_rate >= 55:

            score += 15

        elif win_rate >= 40:

            score += 5

        elif win_rate >= 30:

            score -= 5

        else:

            score -= 10

        # ==========================================
        # Profit Factor
        # ==========================================

        if profit_factor >= 2:

            score += 20

        elif profit_factor >= 1.5:

            score += 10

        elif profit_factor >= 1:

            score += 5

        elif profit_factor >= 0.8:

            score -= 5

        else:

            score -= 10

        # ==========================================
        # Recovery Factor
        # ==========================================

        if recovery > 2:

            score += 15

        elif recovery > 1:

            score += 8

        elif recovery > 0:

            score += 2

        elif recovery > -1:

            score -= 5

        else:

            score -= 10

        # ==========================================
        # Raw Clamp
        # ==========================================

        raw_score = max(
            -20,
            min(
                20,
                score,
            ),
        )

        # ==========================================
        # Apply Sample Size Confidence
        # ==========================================

        adjusted_score = raw_score * sample_factor

        adjusted_score = round(
            adjusted_score,
            2,
        )

        # ==========================================
        # Debug
        # ==========================================

        print("=" * 60)
        print("OPTIMIZER DEBUG")
        print("Experience       :", experience)
        print("Sample Factor    :", sample_factor)
        print("Win Rate         :", win_rate)
        print("Profit Factor    :", profit_factor)
        print("Recovery         :", recovery)
        print("Raw Score        :", raw_score)
        print("Adjusted Score   :", adjusted_score)
        print("=" * 60)

        return adjusted_score