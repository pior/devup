from .base import Command
from .tasks.devup import Devup


class Init(Command):
    name = 'init'
    description = 'Configure this project for DevUp'
    tasks = [Devup]
