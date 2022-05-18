from dataclasses import dataclass
from todoist_api_python.api import Project

@dataclass
class State:
    current_project: Project
    tasks: list

    def set_project(self, project: Project):
        self.current_project = project

    def set_tasks(self, tasks: list):
        self.tasks = tasks
