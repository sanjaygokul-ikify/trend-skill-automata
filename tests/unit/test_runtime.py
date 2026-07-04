import unittest
from packages.core.engine import Engine

class TestRuntime(unittest.TestCase):
    def test_engine(self):
        engine = Engine(None)
        session_logs = [{'action': 'test', 'context': {'key': 'value'}}]
        patterns = engine.extract_patterns(session_logs)
        rules = engine.compile_rules(patterns)
        self.assertEqual(len(patterns), 1)
        self.assertEqual(len(rules), 1)
