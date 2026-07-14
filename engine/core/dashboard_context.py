"""
Dashboard Context
Version 1.0
"""

from data.crypto import get_crypto_prices

from trading.trade_manager import get_current_trade
from trading.trade_statistics import calculate_trade_statistics

from memory.memory_database import load_memory

from backtest.backtest_engine import BacktestEngine
from backtest.performance import PerformanceAnalyzer


class DashboardContext:

    def build(self):

        prices = get_crypto_prices()

        btc_price = prices["BTC"]["price"]

        trade = get_current_trade()

        trade_stats = None

        if trade:

            trade_stats = calculate_trade_statistics(

                trade,

                btc_price,

            )

        memory = load_memory()

        backtest = BacktestEngine()

        results = backtest.load_results()

        performance = PerformanceAnalyzer().calculate(

            results

        )

        return {

            "prices": prices,

            "btc_price": btc_price,

            "trade": trade,

            "trade_stats": trade_stats,

            "memory": memory,

            "performance": performance,

        }