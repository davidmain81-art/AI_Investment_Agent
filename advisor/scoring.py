def calculate_final_score(
    market_score,
    confidence,
    risk,
):
    """
    Calculate a weighted final score
    for comparing investment markets.
    """

    risk_scores = {
        "LOW": 100,
        "MEDIUM": 60,
        "HIGH": 20,
    }

    risk_score = risk_scores.get(risk, 50)

    final_score = (
        market_score * 0.40
        + confidence * 0.35
        + risk_score * 0.25
    )

    return round(final_score, 2)