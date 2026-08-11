from trading import trade_monitor


def test_trade_monitor_buy_take_profit(monkeypatch):

    trade = {
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

    monitor = trade_monitor.TradeMonitor.__new__(
        trade_monitor.TradeMonitor
    )

    monkeypatch.setattr(
        monitor,
        "check_open_trade",
        lambda: trade,
    )

    update_calls = []

    def fake_update_trade_result(
        trade_id,
        exit_price,
        pnl,
        exit_reason,
    ):
        update_calls.append(
            {
                "trade_id": trade_id,
                "exit_price": exit_price,
                "pnl": pnl,
                "exit_reason": exit_reason,
            }
        )

    monkeypatch.setattr(
        trade_monitor,
        "update_trade_result",
        fake_update_trade_result,
    )

    prediction_calls = []

    def fake_save_prediction_result(
        prediction_id,
        exit_price,
        pnl,
        success,
    ):
        prediction_calls.append(
            {
                "prediction_id": prediction_id,
                "exit_price": exit_price,
                "pnl": pnl,
                "success": success,
            }
        )

    monkeypatch.setattr(
        trade_monitor,
        "save_prediction_result",
        fake_save_prediction_result,
    )

    close_calls = []

    def fake_close_trade(trade_id):
        close_calls.append(trade_id)

    monkeypatch.setattr(
        trade_monitor,
        "close_trade",
        fake_close_trade,
    )

    result = monitor.check_price(111.0)

    assert result == "TAKE_PROFIT"

    assert len(update_calls) == 1
    assert update_calls[0]["trade_id"] == 100
    assert update_calls[0]["exit_price"] == 111.0
    assert update_calls[0]["pnl"] == 11.0
    assert update_calls[0]["exit_reason"] == "TAKE_PROFIT"

    assert len(prediction_calls) == 1
    assert prediction_calls[0]["prediction_id"] == 200
    assert prediction_calls[0]["exit_price"] == 111.0
    assert prediction_calls[0]["pnl"] == 11.0
    assert prediction_calls[0]["success"] == 1

    assert close_calls == [100]
def test_trade_monitor_strong_buy_take_profit(monkeypatch):

    trade = {
        "id": 101,
        "prediction_id": 201,
        "asset": "BTC",
        "signal": "STRONG BUY",
        "entry_price": 100.0,
        "stop_loss": 95.0,
        "take_profit": 110.0,
        "confidence": 80,
        "status": "OPEN",
    }

    monitor = trade_monitor.TradeMonitor.__new__(
        trade_monitor.TradeMonitor
    )

    monkeypatch.setattr(
        monitor,
        "check_open_trade",
        lambda: trade,
    )

    monkeypatch.setattr(
        trade_monitor,
        "update_trade_result",
        lambda *args, **kwargs: None,
    )

    monkeypatch.setattr(
        trade_monitor,
        "save_prediction_result",
        lambda *args, **kwargs: None,
    )

    close_calls = []

    def fake_close_trade(trade_id):

        close_calls.append(trade_id)

    monkeypatch.setattr(
        trade_monitor,
        "close_trade",
        fake_close_trade,
    )

    result = monitor.check_price(111.0)

    assert result == "TAKE_PROFIT"
    assert close_calls == [101]