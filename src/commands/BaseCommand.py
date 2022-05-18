from todoist_api_python.api import TodoistAPI
from state import State
class BaseCommand:
    def __init__(self, api: TodoistAPI, name: str):
        self.api = api
        self.name = name
        self.on_initialize()
    
    def on_initialize(self):
        pass

    def on_command(self, args: list, state: State):
        pass
