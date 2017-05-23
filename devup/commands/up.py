from devup.commands import Command
from devup.tasks.python import SetuptoolsDevelop, PipRequirements


class Up(Command):
    description = 'Setup and maintain your development environment'
    _tasks = [SetuptoolsDevelop, PipRequirements]
