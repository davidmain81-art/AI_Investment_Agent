from portfolio.allocation import allocate_assets
from portfolio.capital import CAPITAL, CURRENCY


def build_portfolio(decision):

    allocation = allocate_assets(decision)

    portfolio = {}

    for asset, percent in allocation.items():

        portfolio[asset] = {
            "percent": percent,
            "amount": CAPITAL * percent / 100,
        }

    return {
        "recommendation": decision["recommendation"],
        "market_score": decision["market_score"],
        "confidence": decision["confidence"],
        "currency": CURRENCY,
        "capital": CAPITAL,
        "portfolio": portfolio,
    }