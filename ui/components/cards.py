import streamlit as st


def metric_card(title, value, delta=None):

    with st.container(border=True):

        st.subheader(title)

        st.markdown(
            f"<h2 style='margin:0'>{value}</h2>",
            unsafe_allow_html=True,
        )

        if delta is not None:
            st.caption(delta)