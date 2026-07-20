import unittest
from ..core import Engine
from ..services.orchestrator import OrchestratorService

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        engine = Engine({})
        orchestrator = OrchestratorService(engine)
        agent_id = 'agent-1'
        agent = Engine.Agent(agent_id, 'Agent 1')
        orchestrator.add_agent(agent_id, agent)
        task_id = 'task-1'
        task = Engine.Task(task_id, agent_id, 'Task 1')
        engine.add_task(task_id, task)
        result = engine.execute_task(task_id)
        self.assertIsInstance(result, Engine.Result)