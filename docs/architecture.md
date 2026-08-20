# AI Investment Agent v0.9.6
# System Architecture

Last Update:
2026-08-20

Version:
v0.9.6 Stable Architecture


# Overview

AI Investment Agent is a modular investment analysis system designed for:

- Market Analysis
- AI Decision Making
- Risk Management
- Paper Trading
- Experience Learning
- Performance Evaluation


# Main Architecture


Market Data

â†“

Market Service

â†“

Analysis Engine

â†“

Decision Engine

â†“

Execution Safety

â†“

Trade Service

â†“

Trade Lifecycle

â†“

Memory System

â†“

Learning Engine

â†“

Backtest


# Market Layer

Responsibilities:

- Receive market data
- Normalize data
- Provide candle information


Components:

- Binance Candle Provider
- Market Service
- Market Router


Supported Markets:

- Crypto
- Precious Metals
- Iran Stock Market


# Analysis Layer

Components:

- Indicators Engine
- Market Score
- AI Score Engine
- Confidence Engine
- Pattern Engine
- AI Optimizer


Indicators:

- RSI
- MFI
- EMA20
- EMA50
- EMA200
- MACD
- ATR
- ADX
- OBV
- VWAP


# Decision Engine

The Decision Engine combines:

- Market Signal
- Risk
- AI Score
- Confidence
- Learning Data
- Pattern Score


Output:

- Recommendation
- Confidence
- Position Size
- Risk Information


# Risk Management

Components:

- Risk Manager
- Execution Safety


Purpose:

Prevent unsafe trades before execution.


# Trading Layer

Components:

- Trade Service
- Trade Manager
- Trade Lifecycle


Supported:

- Create Trade
- Monitor Trade
- Take Profit
- Stop Loss
- Reverse Signal
- Close Trade


# Memory System

Memory Database stores:

- Asset
- Signal
- Entry Price
- Exit Price
- PnL
- Result
- Lesson


Purpose:

Create historical experience.


# Learning Engine

Learning Engine analyzes:

- Win Rate
- Profit Factor
- Expectancy
- Drawdown
- Best Asset
- Best Signal
- Trading Experience


Learning Flow:


Trade Result

â†“

Memory Database

â†“

Learning Engine

â†“

Future Decisions


# Backtest Architecture


Closed Trades

â†“

Backtest Engine

â†“

Performance Analyzer

â†“

Performance Report


# Current Status

Version:

v0.9.6 Stable


Tests:

39 Passed


Git:

Master branch clean


# Development Rule

Do not change core architecture without validation.

New features must be added as independent modules.
