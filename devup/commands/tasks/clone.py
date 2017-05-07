# -*- coding: utf-8 -*-
from pathlib import Path

from . import Task, TaskShoudNotRun
from devup.repo import GithubRepo
from devup.project import Project


class GithubClone(Task):
    arguments = ['repository']
    action_message = 'Cloning repository from github'

    def _init(self):
        self._repo = GithubRepo.from_location(self._arg)
        self._project = Project.from_repo(self._repo)

    def should_run(self):
        if self._project.exists():
            path = self._project.local_path
            return TaskShoudNotRun("project already exists in %s" % path)
        return True

    def run(self):
        Path(self._project.local_path).parent.mkdir(exist_ok=True)
        self._run_command(
            ['git', 'clone', self._repo.location, self._project.local_path],
        )
