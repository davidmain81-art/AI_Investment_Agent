import streamlit as st


def dashboard_header():

    left, right = st.columns([4, 1])

    with left:

        st.markdown("""
        # 🤖 AI Investment Agent

        ### Real-Time Investment Terminal
        """)

    with right:

        st.success("🟢 LIVE")