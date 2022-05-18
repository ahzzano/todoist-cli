import sys
from todoist_api_python.api import TodoistAPI
import commands
from state import State

api_key = sys.argv[1]
api = TodoistAPI(api_key)

commands = [commands.Projects(api, 'project'), commands.Tasks(api, 'tasks')]
state = State()

'''
TODO

Important
1. Commands

> project
   > project get tasks
   > project get sections
   > project <section name> tasks 
   > project <section name> <task> complete
   > project <section name> <task> remove
> tasks
    > tasks <task name> complete
    > tasks <task name> remove
> inbox

2. API Response
3. Yeah
'''

if __name__ == '__main__':
    while True: 
        user_input = input('> ')
        user_input_list = user_input.split()
        for c in commands: 
            if user_input_list[0] == c.name:
                c.on_command(user_input_list)
            
            if(user_input_list[0] == 'exit'):
                exit()