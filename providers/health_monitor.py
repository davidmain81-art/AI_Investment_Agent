import time
import requests


class HealthMonitor:


    def check_binance(self):

        start = time.time()

        try:

            response = requests.get(
                "https://api.binance.com/api/v3/ping",
                timeout=10
            )

            latency = round(
                (time.time() - start) * 1000,
                2
            )

            if response.status_code == 200:

                return {
                    "name": "BINANCE",
                    "status": "ONLINE",
                    "latency": latency,
                }


        except Exception as e:

            return {
                "name": "BINANCE",
                "status": "OFFLINE",
                "latency": 0,
                "error": str(e),
            }


        return {
            "name": "BINANCE",
            "status": "OFFLINE",
            "latency": 0,
        }



    def check_system(self):

        return {

            "AI Engine": "READY",

            "Learning Engine": "READY",

            "Optimizer": "READY",

            "Memory": "READY",

        }