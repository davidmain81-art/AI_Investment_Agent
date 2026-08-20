# AI Investment Agent v0.9.6
# Database Schema

Last Update:
2026-08-20

Database:
investment_agent.db


# Overview

The database stores:

- Market History
- AI Predictions
- Trading Operations
- AI Memory
- Learning Features


# Database Flow

Market Data

↓

market_history

↓

Decision Engine

↓

predictions

↓

Trade Execution

↓

trades

↓

Memory / Learning


# Tables


# market_history

Purpose:

Store market condition history.


Fields:

- id
- created_at

Prices:

- btc
- eth
- bnb
- sol
- xrp

Scores:

- crypto_score
- iran_score

Signals:

- crypto_signal
- iran_signal

- winner


# predictions

Purpose:

Store AI predictions before execution.


Fields:

- id
- created_at
- asset
- prediction
- entry_price
- confidence


# prediction_results

Purpose:

Store prediction outcomes.


Fields:

- id
- prediction_id
- exit_price
- pnl
- success


# trades

Main trading table.


Stores:

- asset
- signal
- entry_price
- stop_loss
- take_profit
- confidence
- status


Lifecycle Fields:

- exit_price
- closed_at
- pnl
- exit_reason
- quantity


Trade Status:

- OPEN
- CLOSED


# ai_memory

Purpose:

Store AI decision history.


Fields:

- asset
- signal
- confidence
- market_score
- risk
- pnl
- result


# trade_features

Purpose:

Store features used by AI.


AI Features:

- ai_score
- confidence
- learning
- optimizer
- pattern_score


Market Features:

- RSI
- MFI
- MACD
- MACD Signal
- EMA20
- EMA50
- EMA200
- ATR
- ADX
- OBV


Purpose:

Prepare historical data for future AI optimization.


# Database Rules

- Never modify production database structure without migration.
- All important changes require testing.
- Preserve historical trading data.