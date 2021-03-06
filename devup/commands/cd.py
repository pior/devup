from devup.commands import Command
from devup.tasks import cd


class Cd(Command):
    name = 'cd'
    description = 'Change directory to a project'
    _tasks = [cd.Cd]
    arguments = cd.Cd.arguments
