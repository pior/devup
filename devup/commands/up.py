from . import Command
from ..tasks.python import SetuptoolsDevelop, PipRequirements


class Up(Command):
    description = 'Setup and maintain your development environment'
    tasks = [SetuptoolsDevelop, PipRequirements]
