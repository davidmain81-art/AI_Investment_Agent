import streamlit as st

from database.trades import get_last_open_trade
from analysis.risk_manager import RiskManager


def live_trade_panel():

    trade = get_last_open_trade()

    st.subheader("📄 Current Trade")

    if trade is None:
        st.info("No Open Trade")
        return

    st.metric("Asset", trade["asset"])
    st.metric("Signal", trade["signal"])
    st.metric("Entry", trade["entry_price"])
    st.metric("Take Profit", trade["take_profit"])
    st.metric("Stop Loss", trade["stop_loss"])
    st.metric("Status", trade["status"])

    st.divider()

    st.subheader("🛡️ Risk Management")

    risk = RiskManager().calculate(
        ai_score=54,
        confidence=50,
        risk="MEDIUM"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Position Size",
            f'{risk["position_size"]}%'
        )

        st.metric(
            "Stop Loss %",
            risk["stop_loss_percent"]
        )

    with col2:
        st.metric(
            "Take Profit %",
            risk["take_profit_percent"]
        )

        st.metric(
            "Portfolio Risk %",
            risk["max_portfolio_risk"]
        )