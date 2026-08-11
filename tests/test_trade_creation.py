from trading import trade_manager


def test_trade_creation(monkeypatch):
    decision = {
        "recommendation": "BUY",
        "position": "10%",
        "confidence": 80,
        "holding": "SWING",
    }

    # No existing OPEN trade
    monkeypatch.setattr(
        trade_manager,
        "get_last_open_trade",
        lambda: None,
    )

    # Fake prediction
    monkeypatch.setattr(
        trade_manager,
        "save_prediction",
        lambda **kwargs: 999,
    )

    # Fake trade creation in database
    def fake_save_trade(**kwargs):
        assert kwargs["asset"] == "TEST_ASSET"
        assert kwargs["signal"] == "BUY"
        assert kwargs["entry_price"] == 100.0
        assert kwargs["stop_loss"] == 95.0
        assert kwargs["take_profit"] == 110.0
        assert kwargs["confidence"] == 80
        assert kwargs["prediction_id"] == 999
        assert kwargs["status"] == "OPEN"

        return 1000

    monkeypatch.setattr(
        trade_manager,
        "save_trade",
        fake_save_trade,
    )

    trade = trade_manager.create_trade(
        asset="TEST_ASSET",
        decision=decision,
        entry_price=100.0,
        stop_loss=95.0,
        take_profit=110.0,
    )

    assert trade is not None
    assert trade["id"] == 1000
    assert trade["prediction_id"] == 999
    assert trade["asset"] == "TEST_ASSET"
    assert trade["signal"] == "BUY"
    assert trade["entry_price"] == 100.0
    assert trade["stop_loss"] == 95.0
    assert trade["take_profit"] == 110.0
    assert trade["confidence"] == 80
    assert trade["position"] == "10%"
    assert trade["holding"] == "SWING"
    assert trade["status"] == "OPEN"