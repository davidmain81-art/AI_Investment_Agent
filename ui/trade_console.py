"""
Trade Console
Version 0.5
"""


def print_current_trade(trade):

    print()

    print("📄 CURRENT TRADE")

    print("-" * 50)

    print(f"ID          : {trade['id']}")

    print(f"Asset       : {trade['asset']}")

    print(f"Signal      : {trade['signal']}")

    print(f"Entry       : {trade['entry']}")

    print(f"Stop Loss   : {trade['stop_loss']}")

    print(f"Take Profit : {trade['take_profit']}")

    if "confidence" in trade:

        print(f"Confidence  : {trade['confidence']}%")

    print(f"Status      : {trade['status']}")