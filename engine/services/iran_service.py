"""
Iran Market Service
Version 1.0
"""

from markets.iran_market import get_iran_market
from markets.iran_score import calculate_iran_score
from markets.iran_decision import analyze_iran_market


class IranService:

    def load(self):

        market = get_iran_market()

        score = calculate_iran_score(

            market

        )

        decision = analyze_iran_market(

            score

        )

        return {

            "market": market,

            "score": score,

            "decision": decision,

        }