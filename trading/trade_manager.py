from engine.trade_pipeline import TradePipeline
from database.predictions import save_prediction
from database.prediction_results import save_prediction_result

from database.trades import (
    save_trade,
    get_last_open_trade,
    close_trade,
)


def calculate_pnl(signal, entry_price, exit_price):
    """
    Calculate trade profit percentage.
    """

    if signal == "BUY":

        pnl = ((exit_price - entry_price) / entry_price) * 100

    else:

        pnl = ((entry_price - exit_price) / entry_price) * 100

    return round(pnl, 2)


def create_trade(
    asset,
    decision,
    entry_price,
    stop_loss,
    take_profit,
):

    # ==========================================
    # HOLD = DO NOTHING
    # ==========================================

    if decision["recommendation"] == "HOLD":

        return get_last_open_trade()

    # ==========================================

    position = decision["position"].replace("%", "").strip()

    try:

        position = float(position)

    except ValueError:

        position = 0

    if position <= 0:

        return None

    current_trade = get_last_open_trade()

    # ==========================================
    # Existing OPEN trade
    # ==========================================

    if current_trade:

        if current_trade["signal"] == decision["recommendation"]:

            return current_trade
        
        return current_trade

        pnl = calculate_pnl(

            current_trade["signal"],

            current_trade["entry_price"],

            exit_price,

        )

        success = pnl > 0

        save_prediction_result(

            current_trade["prediction_id"],

            exit_price,

            pnl,

            success,

        )

        close_trade(

            trade_id=current_trade["id"],

            exit_price=exit_price,

            pnl=pnl,

            exit_reason="Reverse Signal",

        )

    # ==========================================
    # Prediction
    # ==========================================

    prediction_id = save_prediction(

        asset=asset,

        prediction=decision["recommendation"],

        entry_price=entry_price,

        confidence=decision["confidence"],

    )

    # ==========================================
    # Trade
    # ==========================================

    trade_id = save_trade(

        asset=asset,

        signal=decision["recommendation"],

        entry_price=entry_price,

        stop_loss=stop_loss,

        take_profit=take_profit,

        confidence=decision["confidence"],

        prediction_id=prediction_id,

        status="OPEN",

    )

    return {

        "id": trade_id,

        "prediction_id": prediction_id,

        "asset": asset,

        "signal": decision["recommendation"],

        "entry_price": entry_price,

        "stop_loss": stop_loss,

        "take_profit": take_profit,

        "confidence": decision["confidence"],

        "holding": decision["holding"],

        "position": decision["position"],

        "status": "OPEN",

    }


def get_current_trade():

    return get_last_open_trade()