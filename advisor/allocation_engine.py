"""
AI Portfolio Allocation
Version 2.0
"""


def allocate_capital(markets):
    """
    Allocate capital using
    score + confidence.
    """

    allocations = []

    total_weight = 0

    for market in markets:

        confidence = market["confidence"]
        score = market.get("score", 50)

        # امتیاز نهایی
        final_score = (confidence * 0.7) + (score * 0.3)

        if final_score >= 80:
            weight = 60

        elif final_score >= 70:
            weight = 35

        elif final_score >= 60:
            weight = 20

        elif final_score >= 40:
            weight = 10

        else:
            weight = 0

        allocations.append({

            "market": market["market"],

            "signal": market["signal"],

            "confidence": confidence,

            "score": score,

            "final_score": round(final_score, 2),

            "weight": weight,

        })

        total_weight += weight

    if total_weight == 0:
        return allocations

    for item in allocations:

        item["allocation"] = round(

            item["weight"] * 100 / total_weight,

            1,

        )

    return allocations