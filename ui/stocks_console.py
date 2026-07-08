"""
Console Output
Iran Stock Market
"""


def print_stock_ranking(symbols):

    print()

    print("🏛 TOP IRAN STOCKS")

    print("-" * 50)

    for i, symbol in enumerate(symbols, start=1):

        print(

            f"{i}. "

            f"{symbol['symbol']:<12}"

            f"Score "

            f"{symbol['score']:>3}"

            f"   "

            f"{symbol['change']:+.2f}%"

        )