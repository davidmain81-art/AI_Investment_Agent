"""
Dashboard Context
Version 1.3
"""

from engine.services.market_service import MarketService
from engine.services.decision_service import DecisionService
from engine.services.global_service import GlobalService
from engine.iran_engine import IranEngine

from trading.trade_manager import get_current_trade
from trading.trade_statistics import calculate_trade_statistics

from memory.memory_database import load_memory

from backtest.backtest_engine import BacktestEngine
from backtest.performance import PerformanceAnalyzer


class DashboardContext:

    def build(self):

        # ==========================================
        # Crypto Market
        # ==========================================

        market_service = MarketService()

        market = market_service.load()

        prices = market["prices"]

        btc_price = market["btc_price"]

        signal = market["signal"]

        risk = market["risk"]

        market_score = market["market_score"]

        # ==========================================
        # AI Decision
        # ==========================================

        decision = DecisionService().build(

            signal,

            risk,

            market_score,

        )

        from analysis.reasoning_engine import ReasoningEngine

        # ==========================================
        # Current Trade
        # ==========================================

        trade = get_current_trade()

        trade_stats = None

        if trade:

            trade_stats = calculate_trade_statistics(

                trade,

                btc_price,

            )

        # ==========================================
        # Memory
        # ==========================================

        memory = load_memory()

        # ==========================================
        # Backtest
        # ==========================================

        backtest = BacktestEngine()

        results = backtest.load_results()

        performance = PerformanceAnalyzer().calculate(

            results

        )

        # ==========================================
        # Iran Market
        # ==========================================

        iran = IranEngine().run()

        global_service = GlobalService()

        global_market = global_service.compare(

            crypto_decision=decision,

            iran_decision=iran["decision"],

        )

        from advisor.global_advisor import build_market_list
        from advisor.allocation_engine import allocate_capital

        markets = build_market_list(

            decision,
            market_score,

            iran["decision"],
            iran["score"],

        )

        portfolio = allocate_capital(markets)

        # ==========================================
        # Global Recommendation
        # ==========================================

        global_service = GlobalService()

        global_market = global_service.compare(

            crypto_decision=decision,

            iran_decision=iran["decision"],

        )

        # ==========================================
        # Context
        # ==========================================

        return {

            "prices": prices,

            "btc_price": btc_price,

            "trade": trade,

            "trade_stats": trade_stats,

            "memory": memory,

            "performance": performance,

            "iran_market": iran["market"],

            "iran_score": iran["score"],

            "iran_decision": iran["decision"],

            "global_market": global_market,

            "portfolio": portfolio,

            "decision": decision,

            "decision": decision,

        }