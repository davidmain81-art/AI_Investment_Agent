import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)


from learning.pattern_engine import PatternEngine


engine = PatternEngine()


engine.report()


engine.close()