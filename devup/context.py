import subprocess
import sys
from pathlib import Path

from devup.utils import output
from devup.lib.project import Project


class Context(object):
    def __init__(self, args):
        self.args = args

    def set_arg(self, name, value):
        setattr(self.args, name, value)

    @staticmethod
    def write_output(s, style=None):
        output.write(s, style=style)

    @staticmethod
    def run_command(args):
        return subprocess.run(args, check=True)

    def panic(self, msg):
        self.write_output('💥 Crashed: %s\n' % msg, style='error')
        sys.exit(1)

    @property
    def project(self):
        return Project(Path.cwd())
