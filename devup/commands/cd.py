from . import Command
from ..tasks.cd import Cd


class Cd(Command):
    description = 'Change directory to a project'
    tasks = [Cd]
