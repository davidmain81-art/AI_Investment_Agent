"""
Backtest Service
Version 1.0
"""

from backtest.backtest_engine import BacktestEngine
from backtest.performance import PerformanceAnalyzer


class BacktestService:

    def __init__(self):

        self.engine = BacktestEngine()

        self.analyzer = PerformanceAnalyzer()

    def summary(self):

        results = self.engine.load_results()

        return self.analyzer.calculate(results)