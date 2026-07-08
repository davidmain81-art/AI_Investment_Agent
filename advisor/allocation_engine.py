def allocate_capital(markets):
    """
    Allocate capital between markets
    based on confidence.
    """

    allocations = []

    total_weight = 0

    for market in markets:

        confidence = market["confidence"]

        if confidence >= 80:
            weight = 60

        elif confidence >= 70:
            weight = 25

        elif confidence >= 40:
            weight = 15

        else:
            weight = 0

        allocations.append({

            "market": market["market"],

            "signal": market["signal"],

            "confidence": confidence,

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