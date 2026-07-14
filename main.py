"""
AI Investment Agent
Version 2.0
"""

from versions.stable.version import VERSION
from engine.live_engine import LiveEngine


def main():

    engine = LiveEngine(

        interval=60

    )

    engine.start()


if __name__ == "__main__":

    main()