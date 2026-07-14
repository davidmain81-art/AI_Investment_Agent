"""
AI Portfolio Optimizer
Version 1.0
"""


def optimize_portfolio(

    decision,

    crypto_score,

    iran_score,

):

    recommendation = decision["recommendation"]

    # ==========================
    # BUY
    # ==========================

    if recommendation == "BUY":

        if crypto_score >= iran_score:

            return {

                "BTC": 45,

                "ETH": 20,

                "USDT": 20,

                "GOLD": 10,

                "USD": 5,

            }

        return {

            "BTC": 20,

            "ETH": 10,

            "USDT": 25,

            "GOLD": 30,

            "USD": 15,

        }

    # ==========================
    # HOLD
    # ==========================

    if recommendation == "HOLD":

        return {

            "BTC": 15,

            "ETH": 10,

            "USDT": 45,

            "GOLD": 20,

            "USD": 10,

        }

    # ==========================
    # SELL
    # ==========================

    return {

        "BTC": 0,

        "ETH": 0,

        "USDT": 60,

        "GOLD": 25,

        "USD": 15,

    }