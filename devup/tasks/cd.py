from devup.tasks import Task, TaskFailed
from devup.integration import set_cd_finalizer
from devup.lib.project import Project


def list_projects(projects_path):
    """Return path for all existing local projects.

    >>> list_projects('/home/pior/src')
    [PosixPath('/home/pior/src/github.com/pior/devup')]
    """
    dirs = [
        project
        for source in projects_path.iterdir() if source.is_dir()
        for org in source.iterdir() if org.is_dir()
        for project in org.iterdir() if project.is_dir()
    ]
    return sorted(dirs)


def project_by_name(projects_path, name):
    paths = list_projects(projects_path)
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
