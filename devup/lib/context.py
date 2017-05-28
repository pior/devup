import subprocess
import sys
from pathlib import Path

from devup.utils import output
from devup.lib.project import Project


def _cast_command_arg(arg):
    if isinstance(arg, Path):
        return str(arg)
    else:
        return arg


def _cast_command_args(args):
    return [_cast_command_arg(arg) for arg in args]


class Context(object):
    def __init__(self, args, config):
        self.args = args
        self.config = config

    @staticmethod
    def write_output(s, style=None):
        output.write(s, style=style)

    @staticmethod
    def run_command(args):
        args = _cast_command_args(args)
        return subprocess.run(args, check=True)

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
        return Project(Path.cwd())
