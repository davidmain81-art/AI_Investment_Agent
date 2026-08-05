from engine.services.trade_service import TradeService


def test_trade_blocked_by_execution_safety():

    service = TradeService()

    decision = {
        "recommendation": "STRONG BUY",
        "safety": {
            "allowed": False
        }
    }

    trade, stats = service.execute(
        decision=decision,
        asset="BTC",
        current_price=64000,
        stop_loss=62000,
        take_profit=70000,
    )

    assert trade is None