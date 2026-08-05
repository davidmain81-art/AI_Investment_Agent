import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from analysis.execution_safety import ExecutionSafety


def test_execution_safety():

    safety = ExecutionSafety()

    result = safety.check(
        ai_score=90,
        confidence=80,
        latency=100,
        risk="LOW"
    )

    assert result is not None