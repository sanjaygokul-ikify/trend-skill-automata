from typing import Dict, List

class Pattern:
    def __init__(self, action: str, context: Dict):
        self.action = action
        self.context = context


class Rule:
    def __init__(self, action: str, context: Dict):
        self.action = action
        self.context = context


class Skill:
    def __init__(self, name: str, rules: List[Rule]):
        self.name = name
        self.rules = rules
