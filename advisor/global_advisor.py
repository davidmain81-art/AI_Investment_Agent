"""
Global Market Advisor
Version 1.2
"""


def build_market_list(
    crypto_decision,
    crypto_score,
    iran_decision,
    iran_score,
):

    return [
        {
            "market": "Crypto",
            "signal": crypto_decision["recommendation"],
            "confidence": crypto_decision["confidence"],
            "score": crypto_score,
        },
        {
            "market": "Iran Gold",
            "signal": iran_decision["signal"],
            "confidence": iran_decision["confidence"],
            "score": iran_score,
        },
    ]


def choose_best_market(
    crypto_decision,
    crypto_score,
    iran_decision,
    iran_score,
):

    crypto_final = (
        crypto_decision["confidence"] * 0.7
        + crypto_score * 0.3
    )

    iran_final = (
        iran_decision["confidence"] * 0.7
        + iran_score * 0.3
    )

    if iran_final > crypto_final:

        return {
            "market": "IRAN",
            "signal": iran_decision["signal"],
            "confidence": iran_decision["confidence"],
            "final_score": round(iran_final, 2),
            "crypto_score": round(crypto_final, 2),
            "iran_score": round(iran_final, 2),
            "difference": round(iran_final - crypto_final, 2),
            "reason": "Iran market has the highest final score.",
        }

    if crypto_final > iran_final:

        return {
            "market": "CRYPTO",
            "signal": crypto_decision["recommendation"],
            "confidence": crypto_decision["confidence"],
            "final_score": round(crypto_final, 2),
            "crypto_score": round(crypto_final, 2),
            "iran_score": round(iran_final, 2),
            "difference": round(crypto_final - iran_final, 2),
            "reason": "Crypto market has the highest final score.",
        }

    return {
        "market": "BOTH",
        "signal": "HOLD",
        "confidence": round(
            (
                crypto_decision["confidence"]
                + iran_decision["confidence"]
            ) / 2,
            2,
        ),
        "final_score": round(crypto_final, 2),
        "crypto_score": round(crypto_final, 2),
        "iran_score": round(iran_final, 2),
        "difference": 0,
        "reason": "Both markets have equal final scores.",
    }
