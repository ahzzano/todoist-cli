from dataclasses import dataclass
from todoist_api_python.api import Project

@dataclass
class State:
    current_project: Project

