import subprocess
from pathlib import Path


class Error(Exception):
    pass


class NotFoundError(Error):
    pass


class Failed(Error):
    pass


def _cast_command_arg(arg):
    if isinstance(arg, Path):
        return str(arg)
    else:
        return arg


def _cast_command_args(args):
    return [_cast_command_arg(arg) for arg in args]


def run(args):
    if isinstance(args, list):
        args = _cast_command_args(args)
        shell = False
    else:
        shell = True

    try:
        return subprocess.run(args, check=True, shell=shell)
    except subprocess.CalledProcessError as err:
        if err.returncode == 127:
            raise NotFoundError(err)
        else:
            raise Failed(err)
