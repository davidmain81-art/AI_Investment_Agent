from trading.trade_manager import create_trade
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


def test_create_trade():

    # ------------------------------------------
    # Clean previous OPEN trades
    # ------------------------------------------

    close_all_open_trades()

    # ------------------------------------------
    # Test Decision
    # ------------------------------------------

    decision = {

        "recommendation": "BUY",

        "confidence": 80,

        "position": "10%",

        "holding": "Swing",

        "ai_score": 80,

        "risk": "LOW",

        "market_score": 20,

        # --------------------------------------
        # Execution Safety
        # --------------------------------------

        "safety": {
            "allowed": True,
            "status": "TRADE ALLOWED",
            "reasons": []
        },

        # --------------------------------------
        # Learning
        # --------------------------------------

        "learning": {
            "experience": 0
        },

        "optimizer_used": 5,

        "pattern_score": 70,

        "position_size": 10,

        # --------------------------------------
        # Indicators
        # --------------------------------------

        "indicators": {

            "RSI": 55,

            "MFI": 55,

            "MACD": 100,

            "MACD_SIGNAL": 90,

            "EMA20": 64000,

            "EMA50": 63500,

            "EMA200": 62000,

            "ATR": 500,

            "ADX": 25,

            "OBV": 1000000,

        },
    }

    # ------------------------------------------
    # Create Trade
    # ------------------------------------------

    trade = create_trade(

        asset="TEST_BTC",

        decision=decision,

        entry_price=64000,

        stop_loss=62000,

        take_profit=70000,

    )

    # ------------------------------------------
    # Trade must be created
    # ------------------------------------------

    assert trade is not None

    assert trade["id"] is not None

    assert trade["asset"] == "TEST_BTC"

    assert trade["signal"] == "BUY"

    assert trade["entry_price"] == 64000

    assert trade["stop_loss"] == 62000

    assert trade["take_profit"] == 70000

    assert trade["confidence"] == 80

    assert trade["status"] == "OPEN"

    # ------------------------------------------
    # Verify Database
    # ------------------------------------------

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            asset,
            signal,
            entry_price,
            stop_loss,
            take_profit,
            confidence,
            prediction_id,
            status
        FROM trades
        WHERE id=?
        """,
        (trade["id"],)
    )

    row = cursor.fetchone()

    # ------------------------------------------
    # Verify trade_features
    # ------------------------------------------

    cursor.execute(
        """
        SELECT
            trade_id,
            asset,
            signal,
            entry,
            ai_score,
            confidence,
            pattern_score,
            position_size
        FROM trade_features
        WHERE trade_id=?
        """,
        (trade["id"],)
    )

    features = cursor.fetchone()

    connection.close()

    # ------------------------------------------
    # Assertions
    # ------------------------------------------

    assert row is not None

    assert row[1] == "TEST_BTC"

    assert row[2] == "BUY"

    assert row[3] == 64000

    assert row[4] == 62000

    assert row[5] == 70000

    assert row[6] == 80

    assert row[7] == trade["prediction_id"]

    assert row[8] == "OPEN"

    # ------------------------------------------
    # Feature Assertions
    # ------------------------------------------

    assert features is not None

    assert features[0] == trade["id"]

    assert features[1] == "TEST_BTC"

    assert features[2] == "BUY"

    assert features[3] == 64000

    assert features[4] == 80

    assert features[5] == 80

    assert features[6] == 70

    assert features[7] == 10

    # ------------------------------------------
    # Cleanup
    # ------------------------------------------

    close_all_open_trades()