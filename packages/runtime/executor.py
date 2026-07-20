import logging
from typing import Dict
from ..core.engine import Engine
from ..core.types import Agent, Task, Result
from ..core.exceptions import InvalidAgentError, InvalidTaskError, InvalidResultError


class Executor:
    def __init__(self, engine: Engine):
        self.engine = engine

    def execute(self, task: Task) -> Result:
        try:
            result = self.engine.execute_task(task.task_id)
            return result
        except InvalidTaskError as e:
            logger.error(f"Error executing task: {e}")
            raise
        except InvalidAgentError as e:
            logger.error(f"Error executing task: {e}")
            raise
        except InvalidResultError as e:
            logger.error(f"Error executing task: {e}")
            raise


logger = logging.getLogger(__name__)
