import yaml


class Project(object):
    """Project as locally cloned repository in source directory."""

    def __init__(self, path):
        self.path = path
        self._manifest_data = None

    def exists(self):
        return self.path.exists()

    @property
    def manifest(self):
        return self.path.joinpath('devup.yml')

    @property
    def manifest_data(self):
        """Deserialized data for valid manifest. None otherwise."""
        if self._manifest_data is None:
            try:
                content = yaml.safe_load(self.manifest.open())
                if isinstance(content, dict):
                    self._manifest_data = content
            except FileNotFoundError:
                pass
        return self._manifest_data

    @property
    def command_names(self):
        if not self.manifest_data:
            return []
        return list(self.manifest_data.keys())

    def get_command_config(self, command_name):
        if not self.manifest_data:
            return
        content = yaml.safe_load(self.manifest.open())
        if isinstance(content, dict):
            return content.get(command_name)
