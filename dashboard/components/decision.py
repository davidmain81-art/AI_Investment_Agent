import streamlit as st


def render_decision(ctx):

    decision = ctx["decision"]

    st.subheader("🤖 Current AI Decision")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Recommendation",
            decision["recommendation"],
        )

        st.metric(
            "Confidence",
            f'{decision["confidence"]}%',
        )

    with c2:

        st.metric(
            "Risk",
            decision["risk"],
        )

        st.metric(
            "Market Score",
            decision["market_score"],
        )