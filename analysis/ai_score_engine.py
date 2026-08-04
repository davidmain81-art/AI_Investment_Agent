"""
AI Score Engine
Version 3.0 Pattern Learning Integrated
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
        # Base Score
        # ==========================================

        score = market_score


        # ==========================================
        # Confidence Weight
        # ==========================================

        score += confidence * 0.30



        # ==========================================
        # Learning Weight
        # ==========================================

        score += learning["win_rate"] * 0.15



        # ==========================================
        # Profit Factor
        # ==========================================

        score += min(

            learning["profit_factor"] * 10,

            5

        )



        # ==========================================
        # Pattern Recognition Weight
        # ==========================================

        score += pattern_score * 0.10



        # ==========================================
        # Risk Adjustment
        # ==========================================

        if risk == "LOW":

            score += 5


        elif risk == "MEDIUM":

            score += 2


        else:

            score -= 5



        # ==========================================
        # Optimizer Impact
        # ==========================================

        raw_optimizer_score = optimizer_score


        optimizer_score = max(

            -20,

            min(

                20,

                optimizer_score

            )

        )


        print("Raw Optimizer :", raw_optimizer_score)

        print("Used Optimizer:", optimizer_score)



        score += optimizer_score



        # ==========================================
        # Final Clamp
        # ==========================================

        score = max(

            0,

            min(

                100,

                round(score, 2)

            )

        )



        # ==========================================
        # Debug
        # ==========================================

        print("=" * 60)

        print("AI SCORE DEBUG")

        print("Market Score     :", market_score)

        print("Confidence       :", confidence)

        print("Learning WinRate :", learning["win_rate"])

        print("Profit Factor    :", learning["profit_factor"])

        print("Pattern Score    :", pattern_score)

        print("Optimizer Score  :", optimizer_score)

        print("FINAL AI SCORE   :", score)

        print("=" * 60)



        return score