from devup.tasks import Task, TaskShouldNotRun
from devup.integration import set_cd_finalizer
from devup.lib.project import Project
from devup.lib.repo import GithubRepo


class GithubClone(Task):
    arguments = ['repository']
    action_message = 'Cloning repository from github'

    @property
    def _repo(self):
        return GithubRepo.from_location(self._arg)

    @property
    def _project(self):
        projects_path = self._context.config.projects_path
        path = projects_path.joinpath(*self._repo.local_id)
        return Project(path)

    def _should_run(self):
        if self._project.exists():
            path = self._project.path
            return TaskShouldNotRun("project already exists in %s" % path)
        return True

    def _run(self):
        self._project.path.parent.mkdir(exist_ok=True)
        self._safe_run_command(
            ['git', 'clone', self._repo.location, self._project.path],
        )
        set_cd_finalizer(self._project.path)
