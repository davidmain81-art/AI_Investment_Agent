import os
import sys

ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.divider()

from datetime import datetime

from data.crypto import get_crypto_prices

from trading.trade_manager import (
    get_current_trade,
)

from trading.trade_statistics import (
    calculate_trade_statistics,
)

from memory.memory_database import (
    load_memory,
)

from backtest.backtest_engine import (
    BacktestEngine,
)

from backtest.performance import (
    PerformanceAnalyzer,
)

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(

    page_title="AI Investment Agent",

    page_icon="📈",

    layout="wide",

)

st.title("🤖 AI Investment Agent Dashboard")

st.caption(
    f"Last Update : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
)

st.divider()

# ==========================================
# LOAD MARKET
# ==========================================

prices = get_crypto_prices()

btc = prices["BTC"]
eth = prices["ETH"]
bnb = prices["BNB"]
sol = prices["SOL"]
xrp = prices["XRP"]

btc_price = btc["price"]

# ==========================================
# TOP METRICS
# ==========================================

c1, c2, c3, c4, c5 = st.columns(5)

with c1:

    st.metric(

        "BTC",

        f"{btc['price']:,.2f} $",

        f"{btc['change']:.2f}%"

    )

with c2:

    st.metric(

        "ETH",

        f"{eth['price']:,.2f} $",

        f"{eth['change']:.2f}%"

    )

with c3:

    st.metric(

        "BNB",

        f"{bnb['price']:,.2f} $",

        f"{bnb['change']:.2f}%"

    )

with c4:

    st.metric(

        "SOL",

        f"{sol['price']:,.2f} $",

        f"{sol['change']:.2f}%"

    )

with c5:

    st.metric(

        "XRP",

        f"{xrp['price']:,.3f} $",

        f"{xrp['change']:.2f}%"

    )

st.divider()

# ==========================================
# CURRENT TRADE
# ==========================================

trade = get_current_trade()

trade_stats = None

if trade:

    trade_stats = calculate_trade_statistics(

        trade,

        btc_price,

    )

st.subheader("📄 Current Trade")

if trade:

    left, middle, right = st.columns(3)

    with left:

        st.metric(

            "Asset",

            trade["asset"]

        )

        st.metric(

            "Signal",

            trade["signal"]

        )

        st.metric(

            "Confidence",

            f"{trade['confidence']} %"

        )

    with middle:

        st.metric(

            "Entry",

            round(trade["entry"],2)

        )

        st.metric(

            "Current",

            trade_stats["current_price"]

        )

        st.metric(

            "PnL",

            f"{trade_stats['pnl']} %"

        )

    with right:

        st.metric(

            "Stop Loss",

            round(trade["stop_loss"],2)

        )

        st.metric(

            "Take Profit",

            round(trade["take_profit"],2)

        )

        st.metric(

            "Status",

            trade["status"]

        )

else:

    st.warning("No Open Trade")

st.divider()

# ==========================================
# BTC LIVE CHART
# ==========================================

st.subheader("📈 BTC Live Price")

price_chart = go.Figure()

price_chart.add_trace(

    go.Indicator(

        mode="number+delta",

        value=btc_price,

        number={"prefix":"$"},

        delta={"reference":btc_price*(1-btc["change"]/100)}

    )

)

st.plotly_chart(

    equity_fig,

    width="stretch",

)

st.divider()

# ==========================================
# MEMORY
# ==========================================

st.subheader("🧠 AI Memory")

memory = load_memory()

memory_df = pd.DataFrame(memory)

# ==========================================
# MEMORY TABLE
# ==========================================

if len(memory_df) == 0:

    st.info("No AI memories recorded.")

else:

    st.dataframe(

    memory_df,

    width="stretch",

    hide_index=True,

)

st.divider()

# ==========================================
# AI EXPERIENCE
# ==========================================

st.subheader("🧠 AI Experience")

total_trades = len(memory_df)

wins = 0
losses = 0
total_pnl = 0

if total_trades > 0:

    wins = len(

        memory_df[
            memory_df["result"] == "WIN"
        ]

    )

    losses = len(

        memory_df[
            memory_df["result"] == "LOSS"
        ]

    )

    total_pnl = round(

        memory_df["pnl"].sum(),

        2,

    )

    win_rate = round(

        wins / total_trades * 100,

        2,

    )

else:

    win_rate = 0

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(

        "Experience",

        total_trades,

    )

with c2:

    st.metric(

        "Wins",

        wins,

    )

with c3:

    st.metric(

        "Losses",

        losses,

    )

with c4:

    st.metric(

        "Win Rate",

        f"{win_rate} %",

    )

st.divider()

# ==========================================
# BACKTEST
# ==========================================

st.subheader("📊 Backtest Statistics")

backtest = BacktestEngine()

results = backtest.load_results()

summary = PerformanceAnalyzer().calculate(

    results

)

b1, b2, b3, b4 = st.columns(4)

with b1:

    st.metric(

        "Trades",

        summary["trades"],

    )

with b2:

    st.metric(

        "Win Rate",

        f"{summary['win_rate']} %",

    )

with b3:

    st.metric(

        "Profit Factor",

        summary["profit_factor"],

    )

with b4:

    st.metric(

        "Total PnL",

        summary["total_pnl"],

    )

st.divider()

# ==========================================
# PORTFOLIO
# ==========================================

st.subheader("💼 Portfolio Allocation")

portfolio = {

    "BTC":20,

    "ETH":10,

    "USDT":25,

    "GOLD":30,

    "USD":15,

}

pie = go.Figure(

    data=[

        go.Pie(

            labels=list(portfolio.keys()),

            values=list(portfolio.values()),

            hole=.45,

        )

    ]

)

st.plotly_chart(

    pie,

    width="stretch",

)

st.divider()

# ==========================================
# EQUITY CURVE
# ==========================================

st.subheader("📈 Equity Curve")

if len(memory_df) > 0:

    equity = []

    balance = 100

    for pnl in memory_df["pnl"]:

        balance += pnl

        equity.append(balance)

    equity_fig = go.Figure()

    equity_fig.add_trace(

        go.Scatter(

            x=list(range(1, len(equity)+1)),

            y=equity,

            mode="lines+markers",

            name="Equity",

        )

    )

    equity_fig.update_layout(

        height=350,

        xaxis_title="Trades",

        yaxis_title="Balance",

    )

    st.plotly_chart(

        equity_fig,

        use_container_width=True,

    )

else:

    st.info("No Equity Data")

st.divider()

# ==========================================
# TRADE HISTORY
# ==========================================

st.subheader("📜 Trade History")

try:

    from database.database import get_connection

    conn = get_connection()

    history = pd.read_sql(

        """

        SELECT

            id,

            asset,

            signal,

            entry_price,

            exit_price,

            pnl,

            status,

            created_at

        FROM trades

        ORDER BY id DESC

        LIMIT 20

        """,

        conn,

    )

    conn.close()

    if len(history):

  st.dataframe(

    history,

    width="stretch",

    hide_index=True,

)

    else:

        st.info("No Trade History")

except Exception as e:

    st.warning(e)

st.divider()

# ==========================================
# LIVE STATUS
# ==========================================

st.subheader("🟢 System Status")


st.subheader("🕒 Server Time")

st.info(

    datetime.now().strftime(

        "%Y-%m-%d %H:%M:%S"

    )

)

st.divider()

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.success("Engine")

    st.write("Running")

with c2:

    st.success("Database")

    st.write("Connected")

with c3:

    st.success("AI")

    st.write("Ready")

with c4:

    st.success("Dashboard")

    st.write("Online")

st.divider()

# ==========================================
# AUTO REFRESH
# ==========================================

refresh = st.sidebar.slider(

    "Refresh (sec)",

    5,

    120,

    30,

)

st.sidebar.write(

    "Dashboard updates every",

    refresh,

    "seconds"

)

st.sidebar.button(

    "🔄 Refresh Now"

)

st.divider()


st.subheader("🌍 Market Health")

if btc["change"] > 2:

    st.success("Bull Market")

elif btc["change"] > 0:

    st.info("Healthy Market")

else:

    st.error("Weak Market")

st.divider()

# ==========================================
# FOOTER
# ==========================================

st.success(

    "AI Investment Agent Dashboard v2.0"

)

st.caption(

    "Developer : Davood"

)
