import argparse
from ..core import Engine
from ..services.orchestrator import OrchestratorService

def main():
    parser = argparse.ArgumentParser(description='Agent Orchestrator CLI')
    parser.add_argument('--add-agent', type=str, help='Add an agent')
    args = parser.parse_args()

    engine = Engine({})
    orchestrator = OrchestratorService(engine)

    if args.add_agent:
        agent_id, agent_name = args.add_agent.split(',')
        agent = Engine.Agent(agent_id, agent_name)
        orchestrator.add_agent(agent_id, agent)