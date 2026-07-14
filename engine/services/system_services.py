"""
System Services
Version 1.0
"""

from engine.services.market_service import MarketService
from engine.services.iran_service import IranService
from engine.services.global_service import GlobalService
from engine.services.decision_service import DecisionService
from engine.services.portfolio_service import PortfolioService
from engine.services.trade_service import TradeService
from engine.services.learning_service import LearningService
from engine.services.backtest_service import BacktestService
from engine.services.report_service import ReportService
from engine.services.ui_service import UIService
from engine.services.risk_service import RiskService


class SystemServices:

    def __init__(self):

        self.market = MarketService()

        self.iran = IranService()

        self.global_market = GlobalService()

        self.decision = DecisionService()

        self.portfolio = PortfolioService()

        self.trade = TradeService()

        self.learning = LearningService()

        self.backtest = BacktestService()

        self.report = ReportService()

        self.ui = UIService()

        self.risk = RiskService()