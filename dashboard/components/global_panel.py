import streamlit as st


def render_global(ctx):

    g = ctx["global_market"]

    st.subheader("🌍 Global AI Recommendation")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Best Market",
            g["market"],
        )

        st.metric(
            "Signal",
            g["signal"],
        )

        st.metric(
            "Confidence",
            f'{g["confidence"]}%',
        )

    with c2:

        st.metric(
            "Crypto Score",
            g["crypto_score"],
        )

        st.metric(
            "Iran Score",
            g["iran_score"],
        )

        st.metric(
            "Difference",
            g["difference"],
        )

    st.info(g["reason"])