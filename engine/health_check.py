"""
Health Check
Version 1.1
"""

import os


class HealthCheck:

    def run(self):

        report = {}

        report["database"] = os.path.exists(
            "investment_agent.db"
        )

        report["logs"] = os.path.exists(
            "logs"
        )

        report["reports"] = os.path.exists(
            "reports"
        )

        report["dashboard"] = os.path.exists(
            "dashboard"
        )

        report["memory"] = os.path.exists(
            "memory"
        )

        report["engine"] = os.path.exists(
            "engine"
        )

        return report

    def summary(self):

        report = self.run()

        total = len(report)

        healthy = sum(report.values())

        return {

            "total": total,

            "healthy": healthy,

            "failed": total - healthy,

            "health_percent": round(

                healthy / total * 100,

                2,

            )

        }