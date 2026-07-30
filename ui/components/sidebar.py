import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.title("🤖 AI Terminal")

        st.markdown("---")

        st.subheader("Portfolio")

        st.progress(15/100)
        st.write("BTC   15%")

        st.progress(10/100)
        st.write("ETH   10%")

        st.progress(45/100)
        st.write("USDT 45%")

        st.progress(20/100)
        st.write("Gold 20%")

        st.progress(10/100)
        st.write("USD  10%")

        st.markdown("---")

        st.subheader("AI Status")

        st.success("ONLINE")

        st.write("Learning Engine")
        st.write("Optimizer")
        st.write("Memory")