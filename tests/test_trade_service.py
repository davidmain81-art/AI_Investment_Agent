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


def test_trade_blocked_by_execution_safety():

    # ------------------------------------------
    # Clean previous OPEN trades
    # ------------------------------------------

    close_all_open_trades()


    # ------------------------------------------
    # Trade Service
    # ------------------------------------------

    service = TradeService()


    # ------------------------------------------
    # Unsafe Decision
    # ------------------------------------------

    decision = {

        "recommendation": "STRONG BUY",

        "safety": {
            "allowed": False
        },

    }


    # ------------------------------------------
    # Execute
    # ------------------------------------------

    trade, stats = service.execute(

        decision=decision,

        asset="BTC",

        current_price=64000,

        stop_loss=62000,

        take_profit=70000,

    )


    # ------------------------------------------
    # Safety must block new trade
    # ------------------------------------------

    assert trade is None

    assert stats is None