import streamlit as st


def render_market(ctx):

    prices = ctx["prices"]

    cols = st.columns(5)

    assets = ["BTC", "ETH", "BNB", "SOL", "XRP"]

    for col, asset in zip(cols, assets):

        with col:

            price = prices[asset]["price"]

            change = prices[asset]["change"]

            if asset == "XRP":
                value = f"{price:,.3f} $"
            else:
                value = f"{price:,.2f} $"

            st.metric(

                asset,

                value,

                f"{change:.2f}%",

            )