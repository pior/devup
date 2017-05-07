import os
import sys

import pkg_resources


INTEGRATION_SCRIPT = 'files/devup.sh'


def print_instruction():
    filename = pkg_resources.resource_filename(__name__, INTEGRATION_SCRIPT)

    print(
        "You must install the shell integration script in your shell"
        " initialization:\n\n",
        "[ -f %s ] && . %s" % (filename, filename),
        "\n",
    )


def check_shell_integration():
    if 'DEVUP_SHELL' not in os.environ:
        print_instruction()
        sys.exit(1)
