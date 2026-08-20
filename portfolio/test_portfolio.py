import pandas as pd

from analysis.decision_engine import make_decision
from portfolio.advisor import build_portfolio


def test_portfolio():

    # ------------------------------------------
    # Create enough candles for indicators
    # ------------------------------------------

    rows = []

    base_price = 64000

    for i in range(50):

        close = base_price + (i * 50)

        rows.append({
            "open": close - 100,
            "high": close + 200,
            "low": close - 200,
            "close": close,
            "volume": 1000 + (i * 10),
        })

    df = pd.DataFrame(rows)

    df.attrs["asset"] = "BTC"

    # ------------------------------------------
    # Decision
    # ------------------------------------------

    decision = make_decision(
        signal="BUY",
        risk="LOW",
        market_score=70,
        df=df,
    )

    # ------------------------------------------
    # Portfolio
    # ------------------------------------------

    portfolio = build_portfolio(decision)

    print("=" * 40)
    print("PORTFOLIO TEST")
    print("=" * 40)

    print(portfolio)

    # ------------------------------------------
    # Assertions
    # ------------------------------------------

    assert decision is not None

    assert portfolio is not None