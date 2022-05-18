from asyncio import tasks
from commands.BaseCommand import BaseCommand
from state.state import State

class Projects(BaseCommand):
    def on_command(self, args: list, state: State):
        try:
            projects = self.api.get_projects()

            for i in projects:
                sections = self.api.get_sections(project_id=i.id)
                print(f'{i.name}')
                
                for s in sections:

                    tasks_from_section = self.api.get_tasks(section_id=s.id)
                    print(f'--{s.name} ({len(tasks_from_section)})')
                print('\n')

        except Exception as e:
            print(e)