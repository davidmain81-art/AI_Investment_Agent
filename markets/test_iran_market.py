from markets.iran_market import get_iran_market
from markets.iran_score import calculate_iran_score
from markets.iran_decision import analyze_iran_market


def main():

    market = get_iran_market()

    score = calculate_iran_score(market)

    decision = analyze_iran_market(score)

    print("=" * 40)
    print("IRAN MARKET TEST")
    print("=" * 40)

    print()

    print("Gold 18K :", market["gold18"])
    print("USD      :", market["usd"])
    print("Coin     :", market["coin"])

    print()

    print("Market Score :", score)

    print("Signal       :", decision["signal"])

    print("Confidence   :", decision["confidence"])


if __name__ == "__main__":
    main()