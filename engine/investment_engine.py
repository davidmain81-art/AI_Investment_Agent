"""
Investment Engine
Version 1.0 Stable
"""

from engine.services.system_services import SystemServices


class InvestmentEngine:

    def __init__(self):

        self.services = SystemServices()

    def run(self):

        # ==============================
        # Market
        # ==============================

        market = self.services.market.load()

        prices = market["prices"]

        btc_price = market["btc_price"]

        signal = market["signal"]

        risk = market["risk"]

        market_score = market["market_score"]

        df = market["df"]

        # ==============================
        # Decision
        # ==============================

        
        decision = self.services.decision.build(

            signal,

            risk,

            market_score,

            df,

        )
        
        # ==============================
        # Portfolio
        # ==============================

        portfolio = self.services.portfolio.build(

            decision

        )

        # ==============================
        # Iran
        # ==============================

        iran = self.services.iran.load()

        iran_market = iran["market"]

        iran_score = iran["score"]

        iran_decision = iran["decision"]

        # ==============================
        # Global
        # ==============================

        global_result = self.services.global_market.compare(

            decision,

            market_score,

            iran_decision,

            iran_score,

        )

        # ==============================
        # Risk
        # ==============================

        risk_data = self.services.risk.calculate(

            btc_price

        )

        stop_loss = risk_data["stop_loss"]

        take_profit = risk_data["take_profit"]

        # ==============================
        # Trade
        # ==============================

        trade, trade_stats = self.services.trade.execute(

            decision,

            "BTC",

            btc_price,

            stop_loss,

            take_profit,

        )

        # ==============================
        # Backtest
        # ==============================

        backtest_summary = self.services.backtest.summary()

        # ==============================
        # Learning
        # ==============================

        ai_stats = self.services.learning.analyze()

        # ==============================
        # HTML Report
        # ==============================

        self.services.report.create(

            decision,

            portfolio,

            trade,

            ai_stats,

            backtest_summary,

        )

        # ==============================
        # Console UI
        # ==============================

        self.services.ui.render(

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

        )
