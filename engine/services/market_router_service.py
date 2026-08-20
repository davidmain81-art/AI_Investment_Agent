"""
Market Router Service
Version 1.0
"""

from markets.market_router import MarketRouter


class MarketRouterService:

    def __init__(self):
        self.router = MarketRouter()

    def route(self, asset):
        return self.router.route(asset)
