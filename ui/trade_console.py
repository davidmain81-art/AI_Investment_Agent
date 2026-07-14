def print_current_trade(
    trade,
    stats=None,
):
    """
    Print current OPEN trade.
    """

    print()

    print("📄 CURRENT TRADE")

    print("-" * 50)

    print(f"ID          : {trade['id']}")

    print(f"Asset       : {trade['asset']}")

    print(f"Signal      : {trade['signal']}")

    print(f"Entry       : {trade['entry']}")

    print(f"Stop Loss   : {trade['stop_loss']}")

    print(f"Take Profit : {trade['take_profit']}")

    print(f"Confidence  : {trade['confidence']}%")

    print(f"Status      : {trade['status']}")

    if stats:

        print()

        print("LIVE STATUS")

        print(f"Current     : {stats['current_price']}")

        print(f"PnL         : {stats['pnl']} %")

        print(f"To TP       : {stats['distance_tp']} %")

        print(f"To SL       : {stats['distance_sl']} %")