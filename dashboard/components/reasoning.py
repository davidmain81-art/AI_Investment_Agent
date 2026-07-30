import streamlit as st


def render_reasoning(ctx):

    st.subheader("🧠 AI Reasoning")

    reasons = ctx.get("decision", {}).get("reasons", [])

    if not reasons:

        st.info("No reasoning available.")

        return

    for reason in reasons:

        st.write("✅", reason)