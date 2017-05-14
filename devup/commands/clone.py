from . import Command
from ..tasks.clone import GithubClone


class Clone(Command):
    description = 'Clone a github repository'
    tasks = [GithubClone]
