import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from learning.pattern_engine import PatternEngine


def test_pattern_engine():

    engine = PatternEngine()

    result = engine.analyze()

    assert result is not None

    assert "pattern_score" in result

    assert "patterns" in result

    engine.close()