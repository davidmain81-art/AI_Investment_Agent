import streamlit as st


def render_trade(ctx):

    trade = ctx["trade"]

    stats = ctx["trade_stats"]

    st.subheader("📄 Current Trade")

    if trade is None:

        st.warning("No Open Trade")

        return

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(

            "Asset",

            trade["asset"],

        )

        st.metric(

            "Signal",

            trade["signal"],

        )

        st.metric(

            "Confidence",

            f"{trade['confidence']} %",

        )

    with c2:

        st.metric(

            "Entry",

            round(trade["entry"], 2),

        )

        st.metric(

            "Current",

            stats["current_price"],

        )

        st.metric(

            "PnL",

            f"{stats['pnl']} %",

        )

    with c3:

        st.metric(

            "Stop Loss",

            round(trade["stop_loss"], 2),

        )

        st.metric(

            "Take Profit",

            round(trade["take_profit"], 2),

        )

        st.metric(

            "Status",

            trade["status"],

        )