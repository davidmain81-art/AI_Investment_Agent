"""
Learning Service
Version 1.0
"""

from learning.learning_engine import LearningEngine


class LearningService:

    def __init__(self):

        self.engine = LearningEngine()

    def analyze(self):

        return self.engine.analyze()