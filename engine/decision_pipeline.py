"""
Trade Pipeline
Version 1.1
"""

from memory.memory_engine import MemoryEngine


class TradePipeline:

    def __init__(self):

        self.memory = MemoryEngine()

    def process(self, trade):

        print("=" * 60)
        print("TRADE PIPELINE EXECUTED")
        print(trade)
        print("=" * 60)

        if trade is None:
            return

        if trade.get("status") != "CLOSED":
            return

        self.memory.remember_trade(trade)

        print("MEMORY SAVED")