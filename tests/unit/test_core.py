import unittest
from packages.core.types import Pattern, Rule, Skill
from packages.core.engine import Engine, PatternMiner, RuleEngine

class TestCore(unittest.TestCase):
    def test_pattern_miner(self):
        miner = PatternMiner()
        session_logs = [{'action': 'test', 'context': {'key': 'value'}}]
        patterns = miner.extract_patterns(session_logs)
        self.assertEqual(len(patterns), 1)
        self.assertIsInstance(patterns[0], Pattern)

    def test_rule_engine(self):
        engine = RuleEngine()
        pattern = Pattern('test', {'key': 'value'})
        rule = engine.compile_rules([pattern])[0]
        self.assertIsInstance(rule, Rule)
        self.assertTrue(engine.execute_rule(rule, {'key': 'value'}))
