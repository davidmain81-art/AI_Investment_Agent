from analysis.decision_engine import make_decision
from portfolio.advisor import build_portfolio


decision = make_decision(
    signal="BUY 🟢",
    risk="LOW",
    market_score=70,
)

portfolio = build_portfolio(decision)

print("=" * 40)
print("PORTFOLIO TEST")
print("=" * 40)

print(portfolio)