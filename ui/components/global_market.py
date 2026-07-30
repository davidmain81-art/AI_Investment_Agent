import streamlit as st

from providers.provider_manager import ProviderManager


def global_market_panel():

    manager = ProviderManager()

    manager.connect()

    provider = manager.get_provider()

    data = provider.get_data()


    st.subheader("🌍 GLOBAL MARKET")

    st.caption(
        f"🟢 Data Source : {manager.get_provider_name()}"
    )


    col1, col2, col3 = st.columns(3)


    with col1:
        st.metric(
            "BTC",
            f'{data["BTC"]["price"]:,}',
            f'{data["BTC"]["change"]:+.2f}%'
        )


    with col2:
        st.metric(
            "ETH",
            f'{data["ETH"]["price"]:,}',
            f'{data["ETH"]["change"]:+.2f}%'
        )


    with col3:
        st.metric(
            "BNB",
            f'{data["BNB"]["price"]:,}',
            f'{data["BNB"]["change"]:+.2f}%'
        )


    col1, col2 = st.columns(2)


    with col1:
        st.metric(
            "SOL",
            f'{data["SOL"]["price"]:,}',
            f'{data["SOL"]["change"]:+.2f}%'
        )


    with col2:
        st.metric(
            "XRP",
            data["XRP"]["price"],
            f'{data["XRP"]["change"]:+.2f}%'
        )