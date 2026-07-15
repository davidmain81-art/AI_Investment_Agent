import streamlit as st


def render_iran(ctx):

    market = ctx["iran_market"]

    score = ctx["iran_score"]

    decision = ctx["iran_decision"]

    st.subheader("🇮🇷 Iran Market")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(

            "Gold 18K",

            f'{market["gold18"]["price"]:,.0f} IRR',

            f'{market["gold18"]["change"]:.2f}%',

        )

    with c2:

        st.metric(

            "USD",

            f'{market["usd"]["price"]:,.0f} IRR',

            f'{market["usd"]["change"]:.2f}%',

        )

    with c3:

        st.metric(

            "Coin",

            f'{market["coin"]["price"]:,.0f} IRR',

            f'{market["coin"]["change"]:.2f}%',

        )

    st.divider()

    c4, c5 = st.columns(2)

    with c4:

        st.metric(

            "Iran Score",

            f"{score}/100",

        )

    with c5:

        st.metric(

            "AI Decision",

            decision["signal"],

            f'{decision["confidence"]}%',

        )