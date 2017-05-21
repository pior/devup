from . import Command
from ..tasks.python import SetuptoolsDevelop


class Up(Command):
    description = 'Setup and maintain your development environment'
    tasks = [SetuptoolsDevelop]
