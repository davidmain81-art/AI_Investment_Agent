"""
Decision Service
Version 2.0
"""

from analysis.decision_engine import make_decision


class DecisionService:

    def build(

        self,

        signal,

        risk,

        market_score,

        df,

    ):

        decision = make_decision(

            signal,

            risk,

            market_score,

            df,

        )

        return decision