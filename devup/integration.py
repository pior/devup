import os
import sys
from pathlib import Path

import pkg_resources


INTEGRATION_SCRIPT = 'files/devup.sh'


def called_by_integration_script():
    return 'DEVUP_SHELL' not in os.environ


def get_finalizer_path():
    return os.getenv('DEVUP_FINALIZER_FILE')


def print_instruction():
    filename = pkg_resources.resource_filename(__name__, INTEGRATION_SCRIPT)

    print(
        "You must install the shell integration script in your shell"
        " initialization:\n\n",
        "[ -f %s ] && . %s" % (filename, filename),
        "\n",
    )


def check():
    if not called_by_integration_script():
        print_instruction()
        sys.exit(1)
    if not get_finalizer_path():
        sys.exit('Shell integration error: missing finalizer path')


def set_cd_finalizer(path):
    add_finalizer('cd:%s' % path)


def add_finalizer(action):
    finalizer_path = get_finalizer_path()
    if not finalizer_path:
        return
    file = Path(finalizer_path)
    if not file.exists():
        sys.stderr.write("Finalizer file doesn't exist: %s" % finalizer_path)
        sys.stderr.flush()
        return
    file.write_text('%s\n' % action)
