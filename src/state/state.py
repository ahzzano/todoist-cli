from dataclasses import dataclass
import enum
from todoist_api_python.api import Project

@dataclass
class State:
    current_project: Project
    tasks: list

    def set_project(self, project: Project):
        self.current_project = project

    def set_tasks(self, tasks: list):
        self.tasks = tasks
        self.organize_tasks()

    def organize_tasks(self):
        tasks = self.tasks[:]
        tasks.sort(key=lambda a : not a.parent_id is None)
        task_ids = list(map(lambda t: t.id, tasks))

        for index, task in enumerate(tasks):
            task_id = task.id
            elements_to_move = list(filter(lambda t: t.parent_id == task_id, tasks))
            rerun = False

            if elements_to_move:
                parent_id = elements_to_move[0].parent_id
                parent_object = list(filter(lambda t: t.id == parent_id, tasks))[0]

                start_index = tasks.index(parent_object) + 1
                end_index = start_index + len(elements_to_move)

                current_index = start_index
                for e in elements_to_move:
                    prev_index = tasks.index(e)
                    temp = tasks[current_index]

                    tasks[current_index] = e
                    tasks[prev_index] = temp

                    current_index += 1

                rerun = True
                
        self.tasks = tasks
