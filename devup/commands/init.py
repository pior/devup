from . import Command
from ..tasks.devup import Devup


class Init(Command):
    description = 'Configure this project for DevUp'
    tasks = [Devup]
