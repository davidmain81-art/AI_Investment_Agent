"""
Decision Pipeline
Version 0.1
"""


class DecisionPipeline:

    def __init__(self):

        self.steps = []

    def add_step(

        self,

        name,

        func,

    ):

        self.steps.append(

            {

                "name": name,

                "func": func,

            }

        )

    def run(

        self,

        context,

    ):

        for step in self.steps:

            context = step["func"](context)

        return context