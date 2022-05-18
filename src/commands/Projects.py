from commands.BaseCommand import BaseCommand

class Projects(BaseCommand):
    def on_command(self, args: list):
        try:
            projects = self.api.get_projects()
            filtered_projects = list(filter(lambda c: c.name != 'Inbox', projects))

            for i in filtered_projects:
                print(f'"{i.name}"')

        except Exception as e:
            print(e)