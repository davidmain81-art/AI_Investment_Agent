import streamlit as st
import pandas as pd

from memory.memory_database import load_memory


def trades_table():

    rows = load_memory()

    if len(rows) == 0:
        st.info("No Trade History")
        return

    df = pd.DataFrame(rows)

    cols = [
        "asset",
        "signal",
        "entry_price",
        "exit_price",
        "pnl",
        "result",
    ]

    cols = [c for c in cols if c in df.columns]

    def color_result(x):

        if x == "WIN":
            return "background-color:#14532D;color:white;"

        if x == "LOSS":
            return "background-color:#7F1D1D;color:white;"

        return ""

    styled = (
        df[cols]
        .style
        .map(color_result, subset=["result"])
        .format({
            "entry_price": "{:.2f}",
            "exit_price": "{:.2f}",
            "pnl": "{:.2f}",
        })
    )

    st.subheader("📑 Trade History")

    st.dataframe(
        styled,
        use_container_width=True,
        hide_index=True,
    )