"""
Universal Trading Cost Engine
Version 2.0
"""


class CostEngine:

    DEFAULT_FEES = {
        "CRYPTO": 0.10,   # 0.10%
        "STOCK": 0.35,
        "FOREX": 0.15,
        "GOLD": 0.20,
        "USD": 0.10,
        "COIN": 0.20,
    }

    def calculate(

        self,

        market,

        price=None,

        quantity=1,

    ):

        return self.DEFAULT_FEES.get(

            market.upper(),

            0.20,

        )