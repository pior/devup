import os
from pathlib import Path


def get_projects_path():
    return Path('~/src').expanduser()


def project_path_from_id(local_id):
    path = os.path.join('~', 'src', *local_id)
    return os.path.expanduser(path)


def list_project_dirs():
    base = get_projects_path()
    dirs = [
        l3
        for l1 in base.iterdir() if l1.is_dir()
        for l2 in l1.iterdir() if l2.is_dir()
        for l3 in l2.iterdir() if l3.is_dir()
    ]
    return sorted(dirs)


class Project(object):
    """Project as locally cloned repository in source directory."""

    def __init__(self, path):
        self.path = path

    @classmethod
    def by_repo(cls, repo):
        path = project_path_from_id(repo.local_id)
        return cls(path)

    @classmethod
    def by_name(cls, name):
        paths = list_project_dirs()
        for path in paths:
            if path.parts[-1] == name:
                return cls(path)
        for path in paths:
            if path.parts[-1].startswith(name):
                return cls(path)

    def exists(self):
        return os.path.exists(self.local_path)
