from devup.tasks import Task, TaskFailed
from devup.integration import set_cd_finalizer
from devup.lib.project import Project


def list_project_dirs(projects_path):
    dirs = [
        l3
        for l1 in projects_path.iterdir() if l1.is_dir()
        for l2 in l1.iterdir() if l2.is_dir()
        for l3 in l2.iterdir() if l3.is_dir()
    ]
    return sorted(dirs)


def project_by_name(projects_path, name):
    paths = list_project_dirs(projects_path)
    for path in paths:
        if path.parts[-1] == name:
            return Project(path)
    for path in paths:
        if path.parts[-1].startswith(name):
            return Project(path)


class Cd(Task):
    arguments = ['project']

    def _run(self):
        name = self._arg

        project = project_by_name(self._context.config.projects_path, name)
        if not project:
            raise TaskFailed("Unknown project %s" % name)
        set_cd_finalizer(project.path)
