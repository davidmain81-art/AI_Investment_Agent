from advisor.scoring import calculate_final_score


def choose_best_market(
    crypto_decision,
    iran_decision,
    crypto_market_score,
    iran_market_score,
    crypto_risk,
):
    """
    Compare all markets using weighted scores.
    """

    crypto_score = calculate_final_score(
        crypto_market_score,
        crypto_decision["confidence"],
        crypto_risk,
    )

    iran_score = calculate_final_score(
        iran_market_score,
        iran_decision["confidence"],
        "LOW",
    )

    if iran_score > crypto_score:

        winner = {
            "market": "IRAN 🇮🇷",
            "signal": iran_decision["signal"],
            "confidence": iran_decision["confidence"],
            "score": iran_score,
            "reason": "Iran market has the highest final score.",
        }

    elif crypto_score > iran_score:

        winner = {
            "market": "CRYPTO 🌍",
            "signal": crypto_decision["recommendation"],
            "confidence": crypto_decision["confidence"],
            "score": crypto_score,
            "reason": "Crypto market has the highest final score.",
        }

    else:

        winner = {
            "market": "BOTH",
            "signal": "HOLD 🟡",
            "confidence": crypto_decision["confidence"],
            "score": crypto_score,
            "reason": "Both markets have equal scores.",
        }

    winner["crypto_score"] = crypto_score
    winner["iran_score"] = iran_score
    winner["difference"] = round(
        abs(crypto_score - iran_score),
        2,
    )

    return winner