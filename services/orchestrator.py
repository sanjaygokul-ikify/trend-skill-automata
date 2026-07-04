from packages.core.engine import Engine
from packages.utils.metrics import Metrics

class Orchestrator:
    def __init__(self, engine: Engine, metrics: Metrics):
        self.engine = engine
        self.metrics = metrics

    def process(self, session_logs: list):
        try:
            patterns = self.engine.extract_patterns(session_logs)
            rules = self.engine.compile_rules(patterns)
            self.metrics.increment('patterns_extracted')
            self.metrics.increment('rules_compiled')
        except Exception as e:
            self.metrics.increment('errors')
            raise
