from asyncio import tasks
from commands.BaseCommand import BaseCommand
from state.state import State
from todoist_api_python.api import Project

class Projects(BaseCommand):
    def on_initialize(self):
        self.projects = self.api.get_projects() 
        self.inbox = list(filter(lambda p: p.name == 'Inbox', self.projects))[0]

    def on_command(self, args: list, state: State):
        try:
            if args[1] == 'get':
                if args[2] == 'tasks':
                    sections = self.api.get_sections(project_id=state.current_project.id)
                    for s in sections: 
                        print(s.name)
                        tasks = filter(lambda t: t.section_id == s.id, state.tasks)
                        prev_task = None
                        prev_parent = None
                        current_parent = None
                        level = 1 

                        for t in tasks:
                            if t.parent_id and not current_parent is None:
                                pass

                            elif t.parent_id and current_parent is None:
                                current_parent = list(filter(lambda task: task.id == t.parent_id, state.tasks))[0]
                                level += 1

                            elif t.parent_id and prev_task.id != current_parent.id:
                                current_parent = t
                                level += 1

                            else: 
                                current_parent = None
                                level = 1 

                            print('--' * level + f' {t.content}')

                            prev_task = t


                if args[2] == 'sections':
                    sections = self.api.get_sections(project_id=state.current_project.id)
                    for s in sections: 
                        print(s.name)

            if args[1] == 'list':
                for i in self.projects:
                    sections = self.api.get_sections(project_id=i.id)
                    print(f'{i.name}')
                    
                    for s in sections:
                        tasks_from_section = list(filter(lambda t: t.section_id == s.id, state.tasks))
                        print(f'--{s.name} ({len(tasks_from_section)})')

            if args[1] == 'set':
                project_name = ' '.join(args[2:])
                selected_project = list(filter(lambda p: p.name == project_name, self.projects))
                if len(selected_project) <= 0:
                    print('project not found!')
                    return
                state.set_project(selected_project[0])

            if args[1] == 'unset':
                state.set_project(self.inbox)

        except Exception as e:
            print(e)