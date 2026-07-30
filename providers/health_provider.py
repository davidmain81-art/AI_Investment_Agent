from providers.health_monitor import HealthMonitor


class HealthProvider:


    def get_latency(self):

        health = HealthMonitor().check_binance()

        return health["latency"]



    def get_status(self):

        health = HealthMonitor().check_binance()

        return health