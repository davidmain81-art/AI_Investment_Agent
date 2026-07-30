"""
Trade Pipeline
Version 1.0

تمام معاملات بسته شده فقط از این مسیر عبور می‌کنند.
"""

from memory.memory_engine import MemoryEngine


class TradePipeline:

    def __init__(self):

        self.memory = MemoryEngine()

    def process(self, trade):

        if trade is None:
            return

        if trade.get("status") != "CLOSED":
            return

        self.memory.remember_trade(trade)