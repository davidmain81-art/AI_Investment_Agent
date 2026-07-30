import time


class MarketCache:


    def __init__(self):

        self.data = None
        self.timestamp = 0


    def set(self, data):

        self.data = data

        self.timestamp = time.time()



    def get(self):

        return self.data



    def age(self):

        if self.timestamp == 0:

            return None

        return round(
            time.time() - self.timestamp,
            2
        )



    def is_valid(self, max_age=30):

        if self.data is None:

            return False

        return (
            self.age() <= max_age
        )