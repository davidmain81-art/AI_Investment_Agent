"""
Trading Configuration
Version 1.0
"""

# ============================
# Account
# ============================

INITIAL_CAPITAL = 100_000_000

CURRENCY = "IRR"

# ============================
# Risk
# ============================

MAX_RISK_PER_TRADE = 2

STOP_LOSS_PERCENT = 3

TAKE_PROFIT_PERCENT = 10

# ============================
# Position Size
# ============================

MIN_POSITION = 2

MAX_POSITION = 25

# ============================
# Fees
# ============================

BUY_FEE = 0.001

SELL_FEE = 0.001

# ============================
# AI
# ============================

MIN_CONFIDENCE = 45

STRONG_CONFIDENCE = 75

# ============================
# Backtest
# ============================

MAX_OPEN_TRADES = 1