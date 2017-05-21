from . import Command
from ..tasks import cd


class Cd(Command):
    description = 'Change directory to a project'
    tasks = [cd.Cd]
