"""
Trade Statistics Console
"""


def print_trade_statistics(stats):

    print()

    print("📈 TRADE STATISTICS")

    print("-" * 50)

    print(f"Total Trades : {stats['total']}")

    print(f"Open Trades  : {stats['open']}")

    print(f"Closed       : {stats['closed']}")

    print(f"Wins         : {stats['wins']}")

    print(f"Losses       : {stats['losses']}")

    print(f"Win Rate     : {stats['win_rate']}%")