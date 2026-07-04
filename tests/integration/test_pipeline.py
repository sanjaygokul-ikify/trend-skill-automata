import unittest
from packages.core.engine import Engine
from packages.utils.metrics import Metrics

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        engine = Engine(None)
        metrics = Metrics()
        session_logs = [{'action': 'test', 'context': {'key': 'value'}}]
        patterns = engine.extract_patterns(session_logs)
        rules = engine.compile_rules(patterns)
        skill = Skill('test', rules)
        result = engine.execute_skill(skill, {'key': 'value'})
        self.assertTrue(result)
        self.assertEqual(metrics.counters['patterns_extracted'], 1)
        self.assertEqual(metrics.counters['rules_compiled'], 1)
