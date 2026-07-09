from database.predictions import save_prediction
from database.trades import (
    save_trade,
    get_last_open_trade,
)


def create_trade(
    asset,
    decision,
    entry_price,
    stop_loss,
    take_profit,
):
    """
    Create AI trade only when position > 0.
    """

    position = decision["position"].replace("%", "").strip()

    try:
        position = float(position)
    except ValueError:
        position = 0

    if position <= 0:
        return None

    prediction_id = save_prediction(
        asset=asset,
        prediction=decision["recommendation"],
        entry_price=entry_price,
        confidence=decision["confidence"],
    )

    trade_id = save_trade(
        asset=asset,
        signal=decision["recommendation"],
        entry_price=entry_price,
        stop_loss=stop_loss,
        take_profit=take_profit,
        confidence=decision["confidence"],
        status="OPEN",
    )

    return {
        "id": trade_id,
        "prediction_id": prediction_id,
        "asset": asset,
        "signal": decision["recommendation"],
        "entry": entry_price,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
        "confidence": decision["confidence"],
        "holding": decision["holding"],
        "position": decision["position"],
        "status": "OPEN",
    }


def get_current_trade():
    """
    Return latest OPEN trade.
    """

    return get_last_open_trade()