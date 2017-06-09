import sys
from pathlib import Path

from devup.lib import output, project


class Context(object):
    def __init__(self, args, config):
        self.args = args
        self.config = config

    @staticmethod
    def write_output(s, style=None):
        output.write(s, style=style)

    def crash(self, msg):
        self.write_output('💥 Crashed: %s\n' % msg, style='error')
        sys.exit(1)

    def exit(self, msg, style='error'):
        self.write_output('%s\n' % msg, style='error')
        sys.exit(1)

    def warning(self, msg):
        self.write_output('%s\n' % msg, style='warning')

    @property
    def project(self):
        return project.Project(Path.cwd())
