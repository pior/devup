import os


def project_path_from_id(local_id):
    path = os.path.join('~', 'src', *local_id)
    return os.path.expanduser(path)


class Project(object):
    """Project as locally cloned repository in source directory."""

    def __init__(self, local_path, remote_path):
        self.local_path = local_path
        self.remote_path = remote_path

    @classmethod
    def from_repo(cls, repo):
        local_path = project_path_from_id(repo.local_id)
        return cls(local_path, repo.location)

    def exists(self):
        return os.path.exists(self.local_path)
