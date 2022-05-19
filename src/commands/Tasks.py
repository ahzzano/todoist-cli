from lib2to3.pytree import Base
from commands.BaseCommand import BaseCommand
from state.state import State

class Tasks(BaseCommand):
    def on_command(self, args: list, state: State):
        try:
            task_name = args[1]

            if '"' in args[1]:
                task_name = []

                ind = 0

                for index, i in enumerate(args[1:]):
                    task_name.append(i)
                    ind = index
                    if i[-1] == '"':
                        break

                task_name = ' '.join(task_name)
                task_name = task_name.replace('"', '')

                for i in range(1, len(args) - 1):
                    args.pop(1)

                temp = args[1]
                args[1] = task_name
                args.append(temp)

            

        except Exception as error:
            print(args)
            print(error)