"""
Base Provider

Every market provider must inherit this class.
"""


class BaseProvider:

    def get_data(self):

        raise NotImplementedError(
            "Provider must implement get_data()."
        )