"""
AI Dynamic Weights
Version 0.1
"""

DEFAULT_WEIGHTS = {

    "trend": 30,

    "risk": 20,

    "volume": 20,

    "momentum": 15,

    "confidence": 15,

}


def load_weights():

    return DEFAULT_WEIGHTS.copy()


def normalize(weights):

    total = sum(weights.values())

    if total == 0:

        return weights

    normalized = {}

    for key, value in weights.items():

        normalized[key] = round(

            value * 100 / total,

            2,

        )

    return normalized