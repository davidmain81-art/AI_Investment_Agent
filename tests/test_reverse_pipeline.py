from engine.services.trade_service import TradeService
from trading.trade_manager import get_current_trade
from memory.memory_engine import MemoryEngine


def close_all_open_trades():

    from database.database import get_connection

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


def test_reverse_signal_closes_old_trade_and_opens_new():

    close_all_open_trades()

    service = TradeService()

    # ==========================================
    # Create initial BUY
    # ==========================================

    buy_decision = {

        "recommendation": "BUY",

        "confidence": 80,

        "position": "10",

        "holding": "SHORT",

        "safety": {
            "allowed": True
        },

    }

    buy_trade, _ = service.execute(

        decision=buy_decision,

        asset="TEST_REVERSE_PIPELINE",

        current_price=100,

        stop_loss=95,

        take_profit=110,

    )

    assert buy_trade is not None

    old_trade_id = buy_trade["id"]

    assert buy_trade["status"] == "OPEN"

    # ==========================================
    # Reverse to SELL
    # ==========================================

    sell_decision = {

        "recommendation": "SELL",

        "confidence": 82,

        "position": "10",

        "holding": "SHORT",

        "safety": {
            "allowed": True
        },

    }

    sell_trade, _ = service.execute(

        decision=sell_decision,

        asset="TEST_REVERSE_PIPELINE",

        current_price=100,

        stop_loss=105,

        take_profit=90,

    )

    assert sell_trade is not None

    assert sell_trade["status"] == "OPEN"

    assert sell_trade["signal"] == "SELL"

    assert sell_trade["id"] != old_trade_id

    # ==========================================
    # Verify new OPEN trade
    # ==========================================

    current_trade = get_current_trade()

    assert current_trade is not None

    assert current_trade["id"] == sell_trade["id"]

    assert current_trade["signal"] == "SELL"

    # ==========================================
    # Verify old trade was CLOSED
    # ==========================================

    from database.database import get_connection

    connection = get_connection()
    connection.row_factory = __import__("sqlite3").Row

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            status,
            exit_reason,
            exit_price,
            pnl
        FROM trades
        WHERE id=?
        """,
        (old_trade_id,),
    )

    old_trade = cursor.fetchone()

    connection.close()

    assert old_trade is not None

    assert old_trade["status"] == "CLOSED"

    assert old_trade["exit_reason"] == "Reverse Signal"

    assert old_trade["exit_price"] == 100

    # ==========================================
    # Memory must contain closed trade
    # ==========================================

    memory = MemoryEngine()

    stats = memory.statistics()

    assert stats["total"] >= 1