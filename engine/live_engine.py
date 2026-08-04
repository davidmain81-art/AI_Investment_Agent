"""
Live Engine
Version 1.1
"""

import os
import time
from datetime import datetime

from engine.investment_engine import InvestmentEngine
from utils.logger import log_info


class LiveEngine:

    def __init__(
        self,
        interval=60,
    ):
        self.interval = interval
        self.engine = InvestmentEngine()
        self.running = True

    # ==========================================
    # Write Log
    # ==========================================

    def write_log(
        self,
        message,
    ):

        os.makedirs(
            "logs",
            exist_ok=True,
        )

        with open(
            "logs/live_engine.log",
            "a",
            encoding="utf-8",
        ) as f:

            f.write(
                f"{datetime.now()} : {message}\n"
            )

    # ==========================================
    # Run Once
    # ==========================================

    def run_once(self):

        log_info("Live Engine Cycle Started")

        print("=" * 60)

        now = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        print(now)

        print("=" * 60)

        self.write_log(
            "Engine Started"
        )

        self.engine.run()

        self.write_log(
            "Cycle Finished"
        )

    # ==========================================
    # Start Loop
    # ==========================================

    def start(self):

        print()

        print("LIVE ENGINE STARTED")

        print()

        self.write_log(
            "Live Engine Started"
        )

        while self.running:

            try:

                self.run_once()

            except Exception as e:


                
                print("Engine Error")
                print(e)

                import traceback
                traceback.print_exc()

                self.write_log(
                    str(e)
                )

            print(
                f"\nSleeping {self.interval} seconds...\n"
            )

            time.sleep(
                self.interval
            )

    # ==========================================
    # Stop
    # ==========================================

    def stop(self):

        self.running = False

        self.write_log(
            "Engine Stopped"
        )

        print("Live Engine Stopped")