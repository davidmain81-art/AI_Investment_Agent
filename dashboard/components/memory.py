import streamlit as st
import pandas as pd

from memory.memory_database import load_memory


def render_memory(ctx):

    rows = load_memory()

    df = pd.DataFrame(rows)

    st.subheader("🧠 AI Memory")

    if len(df) == 0:

        st.info("No AI memories.")

        return

    st.dataframe(

        df,

        width="stretch",

        hide_index=True,

    )

    st.subheader("📈 AI Experience")

    total = len(df)

    wins = len(df[df["result"] == "WIN"])

    losses = len(df[df["result"] == "LOSS"])

    total_pnl = round(df["pnl"].sum(), 2)

    win_rate = round(wins / total * 100, 2)

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(

            "Experience",

            total,

        )

    with c2:

        st.metric(

            "Wins",

            wins,

        )

    with c3:

        st.metric(

            "Losses",

            losses,

        )

    with c4:

        st.metric(

            "Win Rate",

            f"{win_rate}%",

        )

    st.metric(

        "Total PnL",

        total_pnl,

    )