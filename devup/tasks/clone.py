from pathlib import Path

from . import Task, TaskShouldNotRun
from ..integration import set_cd_finalizer
from ..lib.project import Project
from ..lib.repo import GithubRepo


class GithubClone(Task):
    arguments = ['repository']
    action_message = 'Cloning repository from github'

    @property
    def _repo(self):
        return GithubRepo.from_location(self._arg)

    @property
    def _project(self):
        return Project.by_repo(self._repo)

    def should_run(self):
        if self._project.exists():
            path = self._project.local_path
            return TaskShouldNotRun("project already exists in %s" % path)
        return True

    def run(self):
        Path(self._project.local_path).parent.mkdir(exist_ok=True)
        self._run_command(
            ['git', 'clone', self._repo.location, self._project.local_path],
        )
        set_cd_finalizer(self._project.local_path)
