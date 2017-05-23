from devup.commands import Command
from devup.tasks.clone import GithubClone


class Clone(Command):
    description = 'Clone a github repository'
    _tasks = [GithubClone]
    arguments = GithubClone.arguments
