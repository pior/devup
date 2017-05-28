from devup.commands import Command
from devup.tasks.python import SetuptoolsDevelop, PipRequirements


class Up(Command):
    name = 'up'
    description = 'Setup and maintain your development environment'
    _tasks = [SetuptoolsDevelop, PipRequirements]
