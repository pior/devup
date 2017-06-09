import re
import sys


# GPL v2 by http://stackoverflow.com/users/4157799/gi-jack
# http://stackoverflow.com/a/26445590

RESET = '\033[0m'
BOLD = '\033[01m'
DISABLE = '\033[02m'
UNDERLINE = '\033[04m'
REVERSE = '\033[07m'
STRIKETHROUGH = '\033[09m'
INVISIBLE = '\033[08m'


class FG:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    LIGHTGREY = '\033[37m'
    DARKGREY = '\033[90m'
    LIGHTRED = '\033[91m'
    LIGHTGREEN = '\033[92m'
    YELLOW = '\033[93m'
    LIGHTBLUE = '\033[94m'
    PINK = '\033[95m'
    LIGHTCYAN = '\033[96m'


class BG:
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    ORANGE = '\033[43m'
    BLUE = '\033[44m'
    PURPLE = '\033[45m'
    CYAN = '\033[46m'
    LIGHTGREY = '\033[47m'


STYLES = {
    'header': FG.YELLOW,
    'bold': BOLD,
    'info': FG.BLUE,
    'success': FG.GREEN,
    'command': FG.ORANGE,
    'error': FG.RED,
    'warning': FG.LIGHTRED,
    'help': FG.CYAN,
}


def write(s, style=None):
    if style and style in STYLES:
        s = '%s%s%s' % (STYLES[style], s, RESET)
    sys.stdout.write(s)
    sys.stdout.flush()


def humanize(string):
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', string)
