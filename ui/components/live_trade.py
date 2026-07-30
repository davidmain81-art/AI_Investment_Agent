import streamlit as st

from database.trades import get_last_open_trade


def live_trade_panel():

    trade = get_last_open_trade()

    st.subheader("📄 Current Trade")

    if trade is None:

        st.info("No Open Trade")

        return

    st.metric(
        "Asset",
        trade["asset"]
    )

    st.metric(
        "Signal",
        trade["signal"]
    )

    st.metric(
        "Entry",
        trade["entry_price"]
    )

    st.metric(
        "Take Profit",
        trade["take_profit"]
    )

    st.metric(
        "Stop Loss",
        trade["stop_loss"]
    )

    st.metric(
        "Status",
        trade["status"]
    )