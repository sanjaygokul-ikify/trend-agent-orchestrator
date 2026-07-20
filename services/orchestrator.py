from ..core import Engine
from ..utils.logging import logger

class OrchestratorService:
    def __init__(self, engine: Engine):
        self.engine = engine

    def add_agent(self, agent_id: str, agent: Engine.Agent):
        try:
            self.engine.add_agent(agent_id, agent)
            logger.info(f'Agent {agent_id} added successfully')
        except Engine.InvalidAgentError as e:
            logger.error(f'Failed to add agent {agent_id}: {e}')