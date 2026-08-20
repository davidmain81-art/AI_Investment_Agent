import sqlite3

from engine.services.trade_service import TradeService


def test_execution_safety_false_creates_no_trade():

    db_path = "investment_agent.db"

    conn = sqlite3.connect(db_path)

    before = conn.execute(
        "SELECT COUNT(*) FROM trades"
    ).fetchone()[0]

    conn.close()

    decision = {
        "recommendation": "BUY",
        "confidence": 80,
        "position": "10%",
        "holding": "Swing",
        "safety": {
            "allowed": False,
            "status": "TRADE BLOCKED",
            "reasons": [
                "TEST: Execution Safety blocked the trade."
            ],
        },
    }

    service = TradeService()

    trade, stats = service.execute(
        decision=decision,
        asset="TEST_GATE",
        current_price=100.0,
        stop_loss=97.0,
        take_profit=110.0,
    )

    conn = sqlite3.connect(db_path)

    after = conn.execute(
        "SELECT COUNT(*) FROM trades"
    ).fetchone()[0]

    conn.close()

    assert trade is None
    assert stats is None
    assert after == before