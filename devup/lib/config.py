from pathlib import Path


class Config(object):
    """Devup global config.global

    >>> config = Config()
    >>> config.projects_path
    /home/michel/src
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

    @property
    def projects_path(self):
        return Path(self._get('PROJECTS_PATH')).expanduser()
