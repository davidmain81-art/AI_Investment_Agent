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


def test_trade_service_reverse_signal():

    # ------------------------------------------
    # Clean previous OPEN trades
    # ------------------------------------------

    close_all_open_trades()

    # ------------------------------------------
    # Create initial BUY trade
    # ------------------------------------------

    service = TradeService()

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

    # ------------------------------------------
    # Reverse: BUY → SELL
    # Price does NOT hit TP/SL
    # ------------------------------------------

    sell_decision = {

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

    sell_trade, _ = service.execute(

        decision=sell_decision,

        asset="BTC",

        current_price=105.0,

        stop_loss=110.0,

        take_profit=95.0,

    )

    # ------------------------------------------
    # Reverse must create SELL
    # ------------------------------------------

    assert sell_trade is not None
    assert sell_trade["signal"] == "SELL"
    assert sell_trade["status"] == "OPEN"

    # ------------------------------------------
    # Only SELL should remain OPEN
    # ------------------------------------------

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT signal, status
        FROM trades
        WHERE status='OPEN'
        ORDER BY id DESC
        LIMIT 1
        """
    )

    current_trade = cursor.fetchone()

    connection.close()

    assert current_trade is not None
    assert current_trade[0] == "SELL"
    assert current_trade[1] == "OPEN"

    # ------------------------------------------
    # Cleanup
    # ------------------------------------------

    close_all_open_trades()