"""
Market Engine
Version 0.5
"""

from data.crypto import get_crypto_prices
from logs.data_logger import save_market_data

from analysis.market_analysis import analyze_market
from analysis.market_score import calculate_market_score
from analysis.decision_engine import make_decision


class MarketEngine:

    def run(self):

        prices = get_crypto_prices()

        save_market_data(prices)

        signal, risk = analyze_market(prices)

        score = calculate_market_score(prices)

        decision = make_decision(

            signal,

            risk,

            score,

        )

        return {

            "prices": prices,

            "signal": signal,

            "risk": risk,

            "score": score,

            "decision": decision,

        }