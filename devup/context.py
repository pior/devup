import subprocess
import sys

from .utils import output
# from .integration import set_cd_finalizer


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

    # def set_cd_finalizer(self, path):
    #     set_cd_finalizer(path)

    def panic(self, msg):
        self.write_output('💥 Crashed: %s\n' % msg, style='error')
        sys.exit(1)
