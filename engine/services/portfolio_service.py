"""
Portfolio Service
Version 1.0
"""

from portfolio.advisor import build_portfolio


class PortfolioService:

    def build(

        self,

        decision,

    ):

        portfolio = build_portfolio(

            decision

        )

        return portfolio