# AI Investment Agent v0.9.6
# Trading Flow Documentation

Last Update:
2026-08-20


# Overview

Trading pipeline describes the complete lifecycle from market analysis to trade memory.


# Trading Pipeline


Market Data

↓

Market Service

↓

Decision Engine

↓

Execution Safety

↓

Trade Service

↓

Trade Lifecycle

↓

Trade Result

↓

Memory System

↓

Learning Engine



# Step 1 - Market Analysis


Market Service collects:

- Binance Candle Data
- Market Prices
- Technical Indicators


Output:

- Signal
- Risk
- Market Score
- OHLC Data



# Step 2 - Decision Engine


Decision Engine evaluates:


- Market Signal
- AI Score
- Confidence
- Pattern Score
- Learning Data
- Risk


Output:


- Recommendation
- Position Size
- Stop Loss
- Take Profit
- Safety Status



# Step 3 - Execution Safety


Before creating trade:


Checks:

- Risk Level
- Confidence
- AI Score
- System Health


If allowed:

Trade creation continues.


If blocked:

No trade is created.



# Step 4 - Trade Lifecycle


Trade states:


OPEN

↓

Monitoring


Possible exits:


- Take Profit
- Stop Loss
- Reverse Signal


↓

CLOSED



# Step 5 - Memory


Closed trades are stored:


- Entry Price
- Exit Price
- PnL
- Result
- Lesson



# Step 6 - Learning


Learning Engine calculates:


- Win Rate
- Profit Factor
- Expectancy
- Drawdown
- Best Signal
- Best Asset



# Design Rule


Every trade must complete the full lifecycle:

Decision

↓

Safety

↓

Execution

↓

Result

↓

Memory

↓

Learning