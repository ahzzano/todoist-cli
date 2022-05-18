import sys
from todoist_api_python.api import TodoistAPI
import commands
from state import State

api_key = sys.argv[1]
api = TodoistAPI(api_key)

commands = [commands.Projects(api, 'project'), commands.Tasks(api, 'tasks')]
state = State(None)

'''
TODO

Important
1. Commands

> project
   > project get tasks
   > project get sections
   > project set <project name>
   > project unset
   > project <section name> tasks 
> tasks
    > tasks <task name> complete
    > tasks <task name> remove
    > tasks create <task name>
> inbox
> refresh

2. API Response
3. Yeah
'''

if __name__ == '__main__':
    inbox = list(filter(lambda p: p.name == 'Inbox', api.get_projects()))
    state.set_project(inbox[0])
    while True: 
        user_input = input(f'({state.current_project.name}) > ')
        user_input_list = user_input.split()
        for c in commands: 
            if user_input_list[0] == c.name:
                c.on_command(user_input_list, state)
            
            if(user_input_list[0] == 'exit'):
                exit()