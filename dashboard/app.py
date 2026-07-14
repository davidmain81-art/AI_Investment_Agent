import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import streamlit as st

from engine.core.dashboard_context import DashboardContext

from dashboard.components.market import render_market
from dashboard.components.trade import render_trade
from dashboard.components.memory import render_memory

st.set_page_config(
    page_title="AI Investment Agent",
    layout="wide",
)

st.title("AI Investment Agent Dashboard")

ctx = DashboardContext().build()

render_market(ctx)
render_trade(ctx)
render_memory(ctx)