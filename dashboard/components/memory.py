import streamlit as st
import pandas as pd


def render_memory(ctx):

    st.subheader("🧠 AI Memory")

    rows = ctx["memory"]

    df = pd.DataFrame(rows)

    if len(df) == 0:

        st.info("No AI memories recorded.")

        return

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True,

    )

    st.subheader("📈 AI Experience")

    total = len(df)

    wins = len(df[df["result"] == "WIN"])

    losses = len(df[df["result"] == "LOSS"])

    total_pnl = round(df["pnl"].sum(), 2)

    win_rate = round(wins / total * 100, 2)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Experience", total)

    c2.metric("Wins", wins)

    c3.metric("Losses", losses)

    c4.metric("Win Rate", f"{win_rate}%")

    st.metric("Total PnL", total_pnl)