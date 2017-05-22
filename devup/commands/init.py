from devup.commands import Command
from devup.tasks.devup import Devup


class Init(Command):
    description = 'Configure this project for DevUp'
    tasks = [Devup]
