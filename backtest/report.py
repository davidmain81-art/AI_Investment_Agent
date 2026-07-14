def print_backtest(result):

    print()

    print("=" * 60)

    print("BACKTEST REPORT")

    print("=" * 60)

    print()

    print("Trades     :", result["trades"])

    print("Wins       :", result["wins"])

    print("Losses     :", result["losses"])

    print("Win Rate   :", result["win_rate"], "%")

    print("Total PnL  :", result["total_pnl"])

    print()