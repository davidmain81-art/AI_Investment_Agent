import streamlit as st

def render_iran_market(ctx):

    st.subheader("🇮🇷 Iran Market")

    iran = ctx["iran_market"]

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Gold 18K",
            f'{iran["gold18"]:,} IRR',
            f'{iran["gold_change"]:+.2f}%'
        )

    with c2:
        st.metric(
            "USD",
            f'{iran["usd"]:,} IRR',
            f'{iran["usd_change"]:+.2f}%'
        )

    with c3:
        st.metric(
            "Coin",
            f'{iran["coin"]:,} IRR',
            f'{iran["coin_change"]:+.2f}%'
        )

    st.metric(
        "Iran AI Signal",
        ctx["iran_decision"]["signal"]
    )