from database.predictions import save_prediction
from database.prediction_results import save_prediction_result

from database.trades import (
    save_trade,
    get_last_open_trade,
    save_trade_features,
)

from database.close_trade import close_trade


def create_trade(
    asset,
    decision,
    entry_price,
    stop_loss,
    take_profit,
    exit_price=None,
):

    # ==========================================
    # SAFETY GATE
    # ==========================================
    #
    # A trade must NEVER be created when
    # ExecutionSafety says it is not allowed.
    #
    # We check this here because create_trade()
    # can be called from multiple places.
    #

    safety = decision.get("safety", {})

    if not safety.get("allowed", False):

        print("=" * 60)
        print("TRADE CREATION BLOCKED")
        print("Execution Safety : NOT ALLOWED")

        reasons = safety.get(
            "reasons",
            ["Execution Safety blocked the trade."]
        )

        print("Reasons:")
        for reason in reasons:
            print(f" - {reason}")

        print("=" * 60)

        return None

    # ==========================================
    # HOLD = DO NOTHING
    # ==========================================

    if decision["recommendation"] == "HOLD":

        return get_last_open_trade()

    # ==========================================
    # Position Validation
    # ==========================================

    position = decision.get(
        "position",
        "0"
    )

    position = str(position).replace(
        "%",
        ""
    ).strip()

    try:

        position = float(position)

    except (ValueError, TypeError):

        position = 0

    if position <= 0:

        print(
            "TRADE BLOCKED: Invalid position size"
        )

        return None

    # ==========================================
    # Existing OPEN Trade
    # ==========================================

    current_trade = get_last_open_trade()

    if current_trade:

        # ======================================
        # Same signal → keep existing trade
        # ======================================

        if current_trade["signal"] == decision["recommendation"]:

            return current_trade

        # ======================================
        # Reverse Signal
        # ======================================

        if exit_price is None:

            exit_price = entry_price

        closed_trade = close_trade(
            trade_id=current_trade["id"],
            exit_price=exit_price,
            exit_reason="Reverse Signal",
        )

        # ======================================
        # Save Prediction Result
        # ======================================

        if closed_trade:

            save_prediction_result(
                current_trade["prediction_id"],
                exit_price,
                closed_trade["pnl"],
                closed_trade.get("result") == "WIN",
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
    # New Trade
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

    # ==========================================
    # Save Entry Features
    # ==========================================

    save_trade_features(

        trade_id=trade_id,

        asset=asset,

        signal=decision["recommendation"],

        entry_price=entry_price,

        stop_loss=stop_loss,

        take_profit=take_profit,

        decision=decision,

    )

    # ==========================================
    # Return Trade
    # ==========================================

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