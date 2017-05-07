# -*- coding: utf-8 -*-
from .base import Command
from .tasks.clone import GithubClone


class Clone(Command):
    name = 'clone'
    description = 'Clone a github repository'
    tasks = [GithubClone]
