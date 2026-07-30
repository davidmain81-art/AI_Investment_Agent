import streamlit as st

from markets.iran_market import get_iran_market


def market_panel():

    data = get_iran_market()

    st.subheader("📈 IRAN MARKET")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "USD",
            f'{data["usd"]["price"]:,}',
            f'{data["usd"]["change"]:+.2f}%'
        )

        st.metric(
            "Gold 18K",
            f'{data["gold18"]["price"]:,}',
            f'{data["gold18"]["change"]:+.2f}%'
        )

    with col2:
        st.metric(
            "Coin",
            f'{data["coin"]["price"]:,}',
            f'{data["coin"]["change"]:+.2f}%'
        )