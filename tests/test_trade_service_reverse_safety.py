from engine.services.trade_service import TradeService
from database.database import get_connection


def close_all_open_trades():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE trades
        SET
            status='CLOSED',
            exit_reason='TEST CLEANUP'
        WHERE status='OPEN'
        """
    )

    connection.commit()
    connection.close()


def get_open_trade():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            signal,
            status
        FROM trades
        WHERE status='OPEN'
        ORDER BY id DESC
        LIMIT 1
        """
    )

    trade = cursor.fetchone()

    connection.close()

    return trade


def test_reverse_signal_blocked_by_execution_safety():

    # ------------------------------------------
    # Clean previous OPEN trades
    # ------------------------------------------

    close_all_open_trades()

    # ------------------------------------------
    # Trade Service
    # ------------------------------------------

    service = TradeService()

    # ------------------------------------------
    # Create initial BUY trade
    # ------------------------------------------

    buy_decision = {

        "recommendation": "BUY",

        "position": "10%",

        "confidence": 80,

        "holding": "SWING",

        "safety": {
            "allowed": True,
            "status": "TRADE ALLOWED",
            "reasons": []
        },

    }

    buy_trade, _ = service.execute(

        decision=buy_decision,

        asset="BTC",

        current_price=100.0,

        stop_loss=95.0,

        take_profit=110.0,

    )

    assert buy_trade is not None
    assert buy_trade["signal"] == "BUY"
    assert buy_trade["status"] == "OPEN"

    original_trade_id = buy_trade["id"]

    # ------------------------------------------
    # Reverse decision = SELL
    # BUT Execution Safety blocks it
    # ------------------------------------------

    sell_decision = {

        "recommendation": "SELL",

        "position": "10%",

        "confidence": 80,

        "holding": "SWING",

        "safety": {
            "allowed": False,
            "status": "TRADE BLOCKED",
            "reasons": [
                "Execution Safety blocked reverse trade."
            ]
        },

    }

    sell_trade, stats = service.execute(

        decision=sell_decision,

        asset="BTC",

        current_price=105.0,

        stop_loss=110.0,

        take_profit=95.0,

    )

    # ------------------------------------------
    # New SELL trade must NOT be created
    # ------------------------------------------

    assert sell_trade is None
    assert stats is None

    # ------------------------------------------
    # Original BUY must remain OPEN
    # ------------------------------------------

    current_trade = get_open_trade()

    assert current_trade is not None
    assert current_trade[0] == original_trade_id
    assert current_trade[1] == "BUY"
    assert current_trade[2] == "OPEN"

    # ------------------------------------------
    # Cleanup
    # ------------------------------------------

    close_all_open_trades()