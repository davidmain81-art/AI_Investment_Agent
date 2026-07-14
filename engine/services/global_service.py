"""
Global Advisor Service
Version 1.0
"""

from advisor.global_advisor import choose_best_market


class GlobalService:

    def compare(

        self,

        crypto_decision,

        iran_decision,

    ):

        return choose_best_market(

            crypto_decision,

            iran_decision,

        )