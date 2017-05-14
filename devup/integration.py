import os
import sys
from pathlib import Path

import pkg_resources


INTEGRATION_SCRIPT = 'files/devup.sh'
FINALIZER_VARIABLE = 'DEVUP_FINALIZER_FILE'


def print_instruction():
    filename = pkg_resources.resource_filename(__name__, INTEGRATION_SCRIPT)

    print(
        "You must install the shell integration script in your shell"
        " initialization:\n\n",
        "[ -f %s ] && . %s" % (filename, filename),
        "\n",
    )


def check():
    if 'DEVUP_SHELL' not in os.environ:
        print_instruction()
        sys.exit(1)


def set_cd_finalizer(path):
    add_finalizer('cd:%s' % path)


def add_finalizer(action):
    finalizer_path = os.getenv(FINALIZER_VARIABLE)
    file = Path(finalizer_path)
    if not file.exists():
        sys.stderr.write("Finalizer file doesn't exist: %s" % finalizer_path)
        sys.stderr.flush()
    file.write_text('%s\n' % action)
