"""
AI Optimizer
Version 2.0 Balanced
"""


class AIOptimizer:

    def optimize(self, learning):

        score = 0


        # ==========================================
        # Win Rate
        # ==========================================

        win_rate = learning["win_rate"]

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

        profit_factor = learning["profit_factor"]

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

        recovery = learning["recovery_factor"]

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
        # Clamp
        # ==========================================

        score = max(
            -20,
            min(
                20,
                score
            )
        )


        print("=" * 60)
        print("OPTIMIZER DEBUG")
        print("Win Rate       :", win_rate)
        print("Profit Factor  :", profit_factor)
        print("Recovery       :", recovery)
        print("Optimizer Score:", score)
        print("=" * 60)


        return score