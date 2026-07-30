import streamlit as st

from providers.health_monitor import HealthMonitor


def health_panel():

    monitor = HealthMonitor()

    binance = monitor.check_binance()

    system = monitor.check_system()


    st.subheader("🩺 SYSTEM HEALTH")


    if binance["status"] == "ONLINE":

        st.success(
            f'🟢 {binance["name"]} ONLINE | Latency: {binance["latency"]} ms'
        )

    else:

        st.error(
            "🔴 Binance OFFLINE"
        )


    for name, status in system.items():

        st.write(
            f"🟢 {name}: {status}"
        )