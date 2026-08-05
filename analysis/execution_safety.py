class ExecutionSafety:


    def check(
        self,
        ai_score,
        confidence,
        latency,
        risk
    ):


        reasons = []


        # ==========================
        # AI SCORE CHECK
        # ==========================

        if ai_score < 60:

            reasons.append(
                "AI score too low"
            )


        # ==========================
        # CONFIDENCE CHECK
        # ==========================

        if confidence < 40:

            reasons.append(
                "Confidence too low"
            )


        # ==========================
        # NETWORK CHECK
        # ==========================

        if latency > 3000:

            reasons.append(
                "Market connection slow"
            )


        # ==========================
        # RISK CHECK
        # ==========================

        if risk == "HIGH":

            reasons.append(
                "Risk level not allowed"
            )



        # ==========================
        # FINAL DECISION
        # ==========================

        if len(reasons) == 0:

            return {

                "allowed": True,

                "status": "TRADE ALLOWED",

                "reasons": []

            }


        else:

            return {

                "allowed": False,

                "status": "TRADE BLOCKED",

                "reasons": reasons

            }