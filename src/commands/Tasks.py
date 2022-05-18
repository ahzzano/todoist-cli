from lib2to3.pytree import Base
from commands.BaseCommand import BaseCommand

class Tasks(BaseCommand):
    def on_command(self, args: list):
        try:
            tasks = self.api.get_tasks()

            sections = {}

            for t in tasks:
                if not t.project_id in sections.keys():
                    sections[t.project_id] = []
                    
                sections[t.project_id].append(t.content)

            print(sections)

        except Exception as error:
            print(error)