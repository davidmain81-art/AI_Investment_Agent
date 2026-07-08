"""
Global Market Advisor

Compare all available markets.
"""


def build_market_list(

    crypto_decision,
    crypto_score,

    iran_decision,
    iran_score,

):

    markets = [

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

    return markets


def choose_best_market(

    crypto_decision,

    iran_decision,

):

    crypto_final = (

        crypto_decision["confidence"] * 0.7

    ) + (

        25 * 0.3

    )

    iran_final = (

        iran_decision["confidence"] * 0.7

    ) + (

        82.5 * 0.3

    )

    if iran_final > crypto_final:

        return {

            "market": "IRAN 🇮🇷",

            "signal": iran_decision["signal"],

            "confidence": iran_decision["confidence"],

            "final_score": round(

                iran_final,

                2,

            ),

            "crypto_score": round(

                crypto_final,

                2,

            ),

            "iran_score": round(

                iran_final,

                2,

            ),

            "difference": round(

                iran_final - crypto_final,

                2,

            ),

            "reason": "Iran market has the highest final score.",

        }

    elif crypto_final > iran_final:

        return {

            "market": "CRYPTO 🌍",

            "signal": crypto_decision["recommendation"],

            "confidence": crypto_decision["confidence"],

            "final_score": round(

                crypto_final,

                2,

            ),

            "crypto_score": round(

                crypto_final,

                2,

            ),

            "iran_score": round(

                iran_final,

                2,

            ),

            "difference": round(

                crypto_final - iran_final,

                2,

            ),

            "reason": "Crypto market has the highest final score.",

        }

    return {

        "market": "BOTH",

        "signal": "HOLD 🟡",

        "confidence": crypto_decision["confidence"],

        "final_score": round(

            crypto_final,

            2,

        ),

        "crypto_score": round(

            crypto_final,

            2,

        ),

        "iran_score": round(

            iran_final,

            2,

        ),

        "difference": 0,

        "reason": "Both markets have similar scores.",

    }