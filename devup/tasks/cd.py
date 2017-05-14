from . import Task, TaskFailed
from ..integration import set_cd_finalizer
from ..lib.project import Project


class Cd(Task):
    arguments = ['project']

    def run(self):
        name = self._arg
        project = Project.by_name(name)
        if not project:
            raise TaskFailed("Unknown project %s" % name)
        set_cd_finalizer(project.local_path)
