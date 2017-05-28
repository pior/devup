
import yaml


class Project(object):
    """Project as locally cloned repository in source directory."""

    def __init__(self, path):
        self.path = path

    def exists(self):
        return self.path.exists()

    @property
    def manifest(self):
        return self.path.joinpath('devup.yml')

    @property
    def config(self):
        return yaml.safe_load(self.manifest.open())
