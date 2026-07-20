import logging
from typing import Dict, List, Tuple
from .types import Agent, Task, Result
from .exceptions import InvalidAgentError, InvalidTaskError, InvalidResultError


class Engine:
    def __init__(self, agents: Dict[str, Agent]):
        self.agents = agents
        self.tasks = {}
        self.results = {}

    def add_agent(self, agent_id: str, agent: Agent):
        if agent_id in self.agents:
            raise InvalidAgentError(f"Agent with id {agent_id} already exists")
        self.agents[agent_id] = agent

    def remove_agent(self, agent_id: str):
        if agent_id not in self.agents:
            raise InvalidAgentError(f"Agent with id {agent_id} does not exist")
        del self.agents[agent_id]

    def add_task(self, task_id: str, task: Task):
        if task_id in self.tasks:
            raise InvalidTaskError(f"Task with id {task_id} already exists")
        self.tasks[task_id] = task

    def remove_task(self, task_id: str):
        if task_id not in self.tasks:
            raise InvalidTaskError(f"Task with id {task_id} does not exist")
        del self.tasks[task_id]

    def execute_task(self, task_id: str) -> Result:
        if task_id not in self.tasks:
            raise InvalidTaskError(f"Task with id {task_id} does not exist")
        task = self.tasks[task_id]
        agent_id = task.agent_id
        if agent_id not in self.agents:
            raise InvalidAgentError(f"Agent with id {agent_id} does not exist")
        agent = self.agents[agent_id]
        result = agent.execute_task(task)
        self.results[task_id] = result
        return result

    def get_result(self, task_id: str) -> Result:
        if task_id not in self.results:
            raise InvalidResultError(f"Result for task with id {task_id} does not exist")
        return self.results[task_id]


logger = logging.getLogger(__name__)
