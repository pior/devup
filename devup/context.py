import subprocess
import sys

from . import colors
from . import commands


STYLES = {
    'header': colors.FG.YELLOW,
    'bold': colors.BOLD,
    'info': colors.FG.BLUE,
    'success': colors.FG.GREEN,
    'command': colors.FG.ORANGE,
    'error': colors.FG.RED,
    'help': colors.FG.CYAN,
}


class Context(object):
    def get_commands(self):
        cmds = [c(self) for c in commands.classes]
        return cmds

    def set_args(self, args):
        self.args = args

    def write_output(self, s, style=None):
        if style:
            s = '%s%s%s' % (STYLES.get(style), s, colors.RESET)
        sys.stdout.write(s)
        sys.stdout.flush()

    def run_command(self, args):
        return subprocess.run(args, check=True)

    def panic(self, msg):
        self.write_output('💥 Crashed: %s\n' % msg, style='error')
        sys.exit(1)
