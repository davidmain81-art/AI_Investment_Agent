"""
Global Advisor Service
Version 1.2
"""

from advisor.global_advisor import choose_best_market


class GlobalService:

    def compare(
        self,
        crypto_decision,
        crypto_score,
        iran_decision,
        iran_score,
    ):

        return choose_best_market(
            crypto_decision,
            crypto_score,
            iran_decision,
            iran_score,
        )
