import time
from collections import defaultdict

class Metrics:
    def __init__(self):
        self.counters = defaultdict(int)
        self.timers = defaultdict(list)

    def increment(self, name: str):
        self.counters[name] += 1

    def time(self, name: str, duration: float):
        self.timers[name].append(duration)
