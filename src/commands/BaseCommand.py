from todoist_api_python.api import TodoistAPI

class BaseCommand:
    def __init__(self, api: TodoistAPI, name: str):
        self.api = api
        self.name = name

    def on_command(self, args: list):
        pass
