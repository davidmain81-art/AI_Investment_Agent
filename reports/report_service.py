"""
Report Service
Version 1.0
"""

from reports.report_generator import ReportGenerator


class ReportService:

    def __init__(self):

        self.generator = ReportGenerator()

    def create(

        self,

        decision,

        portfolio,

        trade,

        ai_stats,

        backtest,

    ):

        return self.generator.generate(

            decision=decision,

            portfolio=portfolio,

            trade=trade,

            ai_stats=ai_stats,

            backtest=backtest,

        )