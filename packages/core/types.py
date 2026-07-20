from typing import Dict, List
from dataclasses import dataclass

@dataclass
class Agent:
    agent_id: str
    name: str

@dataclass
class Task:
    task_id: str
    agent_id: str
    name: str

@dataclass
class Result:
    result_id: str
    task_id: str
    value: str

AgentDict = Dict[str, Agent]
TaskDict = Dict[str, Task]
ResultDict = Dict[str, Result]
