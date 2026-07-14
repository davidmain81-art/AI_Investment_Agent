"""
UI Service
Version 1.0
"""

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

from ui.trade_console import print_current_trade
from ui.ai_console import print_ai_experience
from backtest.report import print_backtest


class UIService:

    def render(

        self,

        prices,
        signal,
        risk,
        market_score,

        decision,

        portfolio,

        iran_market,
        iran_score,
        iran_decision,

        global_result,

        trade,
        trade_stats,

        stop_loss,
        take_profit,

        backtest_summary,

        ai_stats,

    ):

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

        if trade:

            print_current_trade(

                trade,

                trade_stats,

            )

        print_risk(

            stop_loss,

            take_profit,

        )

        print_backtest(

            backtest_summary

        )

        print_ai_experience(

            ai_stats
        )