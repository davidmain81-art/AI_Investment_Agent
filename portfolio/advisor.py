"""
Portfolio Advisor
Version 2.0
"""

from portfolio.optimizer import optimize_portfolio


def build_portfolio(decision):

    crypto_score = decision.get("market_score", 50)

    iran_score = 65

    allocation = optimize_portfolio(

        decision,

        crypto_score,

        iran_score,

    )

    capital = 100_000_000

    portfolio = {

        "capital": capital,

        "allocation": []

    }

    for asset, percent in allocation.items():

        portfolio["allocation"].append(

            {

                "asset": asset,

                "percent": percent,

                "amount": round(

                    capital * percent / 100

                )

            }

        )

    return portfolio