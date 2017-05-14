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
    return dirs


class Project(object):
    """Project as locally cloned repository in source directory."""

    def __init__(self, local_path, remote_path):
        self.local_path = local_path
        self.remote_path = remote_path

    @classmethod
    def from_repo(cls, repo):
        local_path = project_path_from_id(repo.local_id)
        return cls(local_path, repo.location)

    @classmethod
    def from_name(cls, name):
        paths = list_project_dirs()
        for path in paths:
            if path.parts[-1] == name:
                return cls(path, None)
        for path in paths:
            if path.parts[-1].startswith(name):
                return cls(path, None)

    def exists(self):
        return os.path.exists(self.local_path)
