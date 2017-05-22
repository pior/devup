from devup.commands import Command
from devup.tasks import cd


class Cd(Command):
    description = 'Change directory to a project'
    tasks = [cd.Cd]
    arguments = cd.Cd.arguments
