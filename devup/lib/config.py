from pathlib import Path


class Config(object):
    """Devup global config.global

    >>> import os
    >>> config = Config(os.environ)
    >>> config.projects_path
    /home/pior/src
    """

    _VARIABLE_PREFIX = 'DEVUP_'
    _DEFAULTS = {
        'PROJECTS_PATH': '~/src',
    }

    def __init__(self, env):
        self._env = env

    def _get(self, name, default=None):
        value = default or self._DEFAULTS.get(name)
        value = self._env.get(name, value)
        value = self._env.get(self._VARIABLE_PREFIX + name, value)
        if not value:
            raise RuntimeError("Unknown config setting '%s'" % name)
        return value

    def _get_path(self, name, default=None):
        return Path(self._get(name, default=default)).expanduser()

    @property
    def projects_path(self):
        return self._get_path('PROJECTS_PATH')
