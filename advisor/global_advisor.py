def choose_best_market(
    crypto_decision,
    iran_decision,
):
    """
    Compare crypto and Iran markets
    and choose the better investment.
    """

    crypto_confidence = crypto_decision["confidence"]
    iran_confidence = iran_decision["confidence"]

    if iran_confidence > crypto_confidence:

        return {
            "market": "IRAN 🇮🇷",
            "signal": iran_decision["signal"],
            "confidence": iran_confidence,
            "reason": "Iran market has higher confidence.",
        }

    elif crypto_confidence > iran_confidence:

        return {
            "market": "CRYPTO 🌍",
            "signal": crypto_decision["recommendation"],
            "confidence": crypto_confidence,
            "reason": "Crypto market has higher confidence.",
        }

    else:

        return {
            "market": "BOTH",
            "signal": "HOLD 🟡",
            "confidence": crypto_confidence,
            "reason": "Both markets have similar confidence.",
        }