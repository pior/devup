from devup.tasks import Task, TaskFailed
from devup.integration import set_cd_finalizer
from devup.lib.project import Project


class Cd(Task):
    arguments = ['project']

    def _run(self):
        name = self._arg
        project = Project.by_name(name)
        if not project:
            raise TaskFailed("Unknown project %s" % name)
        set_cd_finalizer(project.local_path)
