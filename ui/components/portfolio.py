import streamlit as st


def portfolio_panel():

    st.subheader("💼 Portfolio Allocation")

    portfolio = {
        "BTC": 15,
        "ETH": 10,
        "USDT": 45,
        "Gold": 20,
        "USD": 10,
    }

    for asset, value in portfolio.items():

        col1, col2 = st.columns([2, 5])

        with col1:
            st.write(asset)

        with col2:
            st.progress(value / 100)

        st.caption(f"{value}%")