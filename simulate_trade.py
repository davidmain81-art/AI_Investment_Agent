"""
Trade Simulator
Version 1.0
"""

from memory.memory_engine import MemoryEngine

memory = MemoryEngine()

fake_trade = {
    "asset": "BTC",
    "signal": "BUY",
    "pnl": 8.75,
}

memory.remember_trade(fake_trade)

print("=" * 50)
print("SIMULATION FINISHED")
print("=" * 50)

print(memory.statistics())