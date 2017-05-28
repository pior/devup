from devup.commands import Command
from devup.tasks.devup import Devup


class Init(Command):
    name = 'init'
    description = 'Configure this project for DevUp'
    _tasks = [Devup]
