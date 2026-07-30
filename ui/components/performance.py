import streamlit as st

from learning.learning_engine import LearningEngine


def performance_panel():

    engine = LearningEngine()

    stats = engine.analyze()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Trades",
        stats["experience"]
    )

    c2.metric(
        "Win Rate",
        f'{stats["win_rate"]}%'
    )

    c3.metric(
        "Profit Factor",
        stats["profit_factor"]
    )

    c4.metric(
        "Recovery",
        stats["recovery_factor"]
    )