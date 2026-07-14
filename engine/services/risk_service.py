"""
Risk Service
Version 1.0
"""

from risk.risk_manager import (
    calculate_stop_loss,
    calculate_take_profit,
)


class RiskService:

    def calculate(

        self,

        btc_price,

    ):

        stop_loss = calculate_stop_loss(

            btc_price

        )

        take_profit = calculate_take_profit(

            btc_price

        )

        return {

            "stop_loss": stop_loss,

            "take_profit": take_profit,

        }