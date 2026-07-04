import logging
from typing import Dict
from packages.core.engine import Engine
from packages.core.types import Skill


class Executor:
    def __init__(self, engine: Engine):
        self.engine = engine

    def execute_skill(self, skill: Skill, context: Dict) -> bool:
        try:
            result = self.engine.execute_skill(skill, context)
            return result
        except Exception as e:
            logging.error(f"Skill execution failed: {str(e)}")
            raise
