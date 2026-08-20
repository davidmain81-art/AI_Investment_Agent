from trading import trade_manager


def test_reverse_signal_closes_existing_trade(monkeypatch):

    decision = {
        "recommendation": "SELL",
        "position": "10%",
        "confidence": 80,
        "holding": "SWING",

        "safety": {
            "allowed": True,
            "status": "TRADE ALLOWED",
            "reasons": []
        },
    }

    existing_trade = {
        "id": 100,
        "prediction_id": 200,
        "asset": "BTC",
        "signal": "BUY",
        "entry_price": 100.0,
        "stop_loss": 95.0,
        "take_profit": 110.0,
        "confidence": 80,
        "status": "OPEN",
    }

    monkeypatch.setattr(
        trade_manager,
        "get_last_open_trade",
        lambda: existing_trade,
    )
    
    monkeypatch.setattr(
        trade_manager,
        "save_trade_features",
        lambda **kwargs: None,
    )

    close_calls = []

    def fake_close_trade(**kwargs):

        close_calls.append(kwargs)

        return {
            "id": 100,
            "status": "CLOSED",
            "pnl": 5.0,
        }

    monkeypatch.setattr(
        trade_manager,
        "close_trade",
        fake_close_trade,
    )

    prediction_calls = []

    def fake_save_prediction(**kwargs):

        prediction_calls.append(kwargs)

        return 300

    monkeypatch.setattr(
        trade_manager,
        "save_prediction",
        fake_save_prediction,
    )

    trade_calls = []

    def fake_save_trade(**kwargs):

        trade_calls.append(kwargs)

        return 400

    monkeypatch.setattr(
        trade_manager,
        "save_trade",
        fake_save_trade,
    )

    result = trade_manager.create_trade(
        asset="BTC",
        decision=decision,
        entry_price=105.0,
        stop_loss=110.0,
        take_profit=95.0,
    )

    assert len(close_calls) == 1

    assert close_calls[0]["trade_id"] == 100
    assert close_calls[0]["exit_price"] == 105.0
    assert close_calls[0]["exit_reason"] == "Reverse Signal"

    assert len(prediction_calls) == 1

    assert len(trade_calls) == 1
    assert trade_calls[0]["signal"] == "SELL"

    assert result is not None
    assert result["id"] == 400
    assert result["signal"] == "SELL"
    assert result["status"] == "OPEN"