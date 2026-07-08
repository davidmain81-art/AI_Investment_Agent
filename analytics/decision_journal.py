"""
Decision Journal
Version 0.1

Stores every AI decision.
"""

from datetime import datetime


def build_decision_entry(

    market,

    asset,

    signal,

    confidence,

    score,

    reasons,

):

    return {

        "time": datetime.now().strftime(

            "%Y-%m-%d %H:%M:%S"

        ),

        "market": market,

        "asset": asset,

        "signal": signal,

        "confidence": confidence,

        "score": score,

        "reasons": reasons,

    }