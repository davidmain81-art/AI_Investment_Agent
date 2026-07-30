import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st

from components.styles import load_css
from components.cards import metric_card
from components.charts import equity_curve
from components.sidebar import show_sidebar
from components.portfolio import portfolio_panel
from components.live_trade import live_trade_panel
from components.performance import performance_panel
from components.header import dashboard_header
from components.gauge import ai_gauge
from components.tables import trades_table
from components.market import market_panel
from components.global_market import global_market_panel
from components.health import health_panel
from components.safety import safety_panel

from analysis.decision_engine import make_decision


st.set_page_config(
    page_title="AI Investment Agent",
    page_icon="📈",
    layout="wide"
)


load_css()
show_sidebar()

dashboard_header()


# ===========================================
# REAL AI DECISION
# ===========================================

decision = make_decision(
    signal="HOLD",
    risk="MEDIUM",
    market_score=40
)

learning = decision["learning"]


# ===========================================
# TOP METRICS
# ===========================================

col1, col2, col3, col4 = st.columns(4)


with col1:
    metric_card(
        "AI Score",
        str(decision["ai_score"]),
        ""
    )


with col2:
    metric_card(
        "Win Rate",
        f'{learning["win_rate"]}%',
        ""
    )


with col3:
    metric_card(
        "Open Trades",
        "1",
        ""
    )


with col4:
    metric_card(
        "Net Profit",
        str(learning["net_profit"]),
        ""
    )


st.divider()


# ===========================================
# PERFORMANCE
# ===========================================

performance_panel()


st.divider()

# ===========================================
# EXECUTION SAFETY
# ===========================================

safety_panel(
    decision["safety"]
)


st.divider()




# ===========================================
# MAIN DASHBOARD GRID
# ===========================================

market_left, market_right = st.columns([1, 1])


with market_left:

    global_market_panel()


with market_right:

    market_panel()


st.divider()


ai_left, portfolio_right = st.columns([1, 2])


with ai_left:

    st.plotly_chart(
        ai_gauge(decision["ai_score"]),
        use_container_width=True
    )


with portfolio_right:

    portfolio_panel()



st.divider()

# ===========================================
# SYSTEM HEALTH
# ===========================================

health_panel()



st.divider()



# ===========================================
# EQUITY CURVE
# ===========================================

st.subheader("📊 Equity Curve")


st.plotly_chart(
    equity_curve(),
    use_container_width=True
)



st.divider()


# ===========================================
# CURRENT TRADE
# ===========================================

live_trade_panel()


st.divider()


# ===========================================
# TRADE HISTORY
# ===========================================

trades_table()