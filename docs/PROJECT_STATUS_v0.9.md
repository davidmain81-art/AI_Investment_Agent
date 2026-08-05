# AI Investment Agent
# PROJECT_STATUS_v0.9

Last Update:
2026-08

---

# Project Goal

Develop a professional AI Investment Agent capable of:

- Technical Analysis
- Fundamental Analysis
- Pattern Recognition
- AI Learning
- Capital Management
- Risk Management
- Portfolio Allocation
- Paper Trading
- Live Trading
- Iran Stock Market Integration
- Binance Integration
- Dashboard
- Reporting

---

# Current Progress

Overall Progress

████████████████████░░░░░░░░
≈ 70%

---

# Current Architecture

```
Binance API
      │
      ▼
Binance Candle Provider
      │
      ▼
Market Service
      │
      ▼
Indicators Engine
      │
      ▼
Decision Engine
      │
      ▼
Paper Trading
      │
      ▼
Feature Store
      │
      ▼
Learning Engine
      │
      ▼
AI Optimizer
      │
      ▼
Decision Engine
```

---

# Completed Modules

## Core

- Binance API
- Candle Provider
- Market Service
- Dashboard Context
- Decision Service

---

## Analysis

- Market Analysis
- Market Score
- AI Score Engine
- Confidence Engine
- Decision Engine v7
- AI Optimizer
- Risk Manager
- Execution Safety
- Reasoning Engine
- Indicators Engine

---

## Trading

- Paper Trading

---

## Learning

- Learning Engine
- Experience Manager

---

## Database

- investment_agent.db
- ai_memory.py
- feature_store.py

---

## Dashboard

- Streamlit Dashboard
- Reports
- Performance

---

# Current Indicators

Implemented

- RSI
- MFI
- EMA20
- EMA50
- EMA200
- ATR
- ADX
- MACD
- MACD Signal
- OBV
- VWAP
- Volume
- Spread
- Volatility
- Trend

Prepared Fields

- Funding Rate
- Open Interest
- Fear & Greed
- News Score

---

# Feature Store

Paper Trading currently stores:

## Trade

- Asset
- Signal
- Entry
- Exit
- Stop Loss
- Take Profit
- Position Size
- Result
- PnL

## AI

- AI Score
- Confidence
- Learning
- Optimizer
- Market Score
- Risk

## Indicators

- RSI
- MFI
- EMA20
- EMA50
- EMA200
- ATR
- ADX
- MACD
- MACD Signal
- OBV
- VWAP
- Volume
- Spread
- Volatility
- Trend

## Future

- Funding Rate
- Open Interest
- Fear & Greed
- News Score

---

# AI Memory

Decision Engine stores

- Recommendation
- AI Score
- Confidence
- Risk
- Market Score

---

# Stable Status

The engine is currently stable.

The following pipeline works:

```
Dashboard

↓

Market Service

↓

Indicators

↓

Decision Engine

↓

Paper Trading

↓

Feature Store
```

---

# Current TODO

## HIGH PRIORITY

### 1

Create

```
learning/pattern_engine.py
```

Purpose

- Detect profitable patterns
- Detect losing patterns
- Win Rate
- Profit Factor
- Pattern Score

---

### 2

Integrate Pattern Score into AI Score

```
Pattern Engine

↓

AI Optimizer

↓

Decision Engine
```

---

### 3

Improve Trade Lifecycle

Prevent trade execution when

```
ExecutionSafety.allowed == False
```

---

### 4

Validate all indicator inputs

Need verification for

- RSI
- MFI
- ATR
- ADX
- EMA
- MACD

Ensure values come from real candle data.

---

# Future Roadmap

## Phase 1

Stabilize

- Data Pipeline
- Feature Store
- Learning Engine
- Pattern Engine

---

## Phase 2

Adaptive AI

Indicators become dynamic.

Instead of

```
RSI = weight 10
```

AI should learn

```
RSI = weight 4

MFI = weight 12

SuperTrend = weight 17
```

Automatically.

---

## Phase 3

Massive Paper Trading

Thousands of simulated trades

↓

Learning

↓

Weight Optimization

---

## Phase 4

Live Trading

---

## Phase 5

Iran Stock Market

Integrate

- TSETMC
- Codal
- Rahavard
- IFB

---

## Phase 6

Fundamental Analysis

Automatically read

- Balance Sheet
- Income Statement
- Cash Flow
- EPS
- PE
- NAV
- Dividend
- Capital Increase

from Codal.

---

## Phase 7

Combined AI

Final decision should combine

- Technical
- Fundamental
- Pattern Recognition
- Experience
- Risk
- Capital Allocation
- Macro Economy
- News
- Sentiment
- Fear & Greed

---

# Coding Principles

- Clean Architecture
- Stable before adding new features
- Modular Design
- Version Controlled
- Every module independently testable
- AI learns from experience rather than fixed rules

---

# Next Task

Start implementing

```
learning/pattern_engine.py
```

This is the next milestone before Adaptive AI.