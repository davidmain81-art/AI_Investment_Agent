from database.predictions import save_prediction
from database.trades import save_trade


def create_trade(
    asset,
    decision,
    entry_price,
    stop_loss,
    take_profit,
):
    """
    Create a new AI trade and store it.
    """

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