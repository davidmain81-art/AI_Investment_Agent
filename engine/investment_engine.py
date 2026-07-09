"""
Investment Engine
Version 0.5
"""

from logs.data_logger import save_market_data

from data.crypto import get_crypto_prices

from analysis.market_analysis import analyze_market
from analysis.market_score import calculate_market_score
from analysis.decision_engine import make_decision

from portfolio.advisor import build_portfolio

from markets.iran_market import get_iran_market
from markets.iran_score import calculate_iran_score
from markets.iran_decision import analyze_iran_market

from advisor.global_advisor import choose_best_market

from risk.risk_manager import (
    calculate_stop_loss,
    calculate_take_profit,
)

from ui.console import (
    print_header,
    print_crypto,
    print_analysis,
    print_score,
    print_decision,
    print_portfolio,
    print_iran_market,
    print_global_recommendation,
    print_risk,
)

# مسیر صحیح
from trading.trade_manager import get_current_trade

# اگر این فایل وجود ندارد، فعلاً این import را کامنت کن.
from ui.trade_console import print_current_trade


class InvestmentEngine:

    def run(self):

        prices = get_crypto_prices()

        save_market_data(prices)

        btc_price = prices["BTC"]["price"]

        signal, risk = analyze_market(prices)

        market_score = calculate_market_score(prices)

        decision = make_decision(
            signal,
            risk,
            market_score,
        )

        portfolio = build_portfolio(decision)

        iran_market = get_iran_market()

        iran_score = calculate_iran_score(
            iran_market
        )

        iran_decision = analyze_iran_market(
            iran_score
        )

        global_result = choose_best_market(
            decision,
            iran_decision,
        )

        stop_loss = calculate_stop_loss(
            btc_price
        )

        take_profit = calculate_take_profit(
            btc_price
        )

        current_trade = get_current_trade()

        print_header()

        print_crypto(prices)

        print_analysis(
            signal,
            risk,
        )

        print_score(
            market_score
        )

        print_decision(
            decision
        )

        print_portfolio(
            portfolio
        )

        print_iran_market(
            iran_market,
            iran_score,
            iran_decision,
        )

        print_global_recommendation(
            global_result
        )

        if current_trade:
            print_current_trade(
                current_trade
            )

        print_risk(
            stop_loss,
            take_profit,
        )