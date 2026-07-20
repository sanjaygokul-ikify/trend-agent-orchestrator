import unittest
from ..core import Engine, Agent, Task, Result

class TestCore(unittest.TestCase):
    def test_add_agent(self):
        engine = Engine({})
        agent_id = 'agent-1'
        agent = Agent(agent_id, 'Agent 1')
        engine.add_agent(agent_id, agent)
        self.assertIn(agent_id, engine.agents)

    def test_add_task(self):
        engine = Engine({})
        task_id = 'task-1'
        task = Task(task_id, 'agent-1', 'Task 1')
        engine.add_task(task_id, task)
        self.assertIn(task_id, engine.tasks)