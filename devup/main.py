import argparse
import sys

from .context import Context
from .integration import check_shell_integration


def make_parser(commands):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    for command in commands:
        sub = subparsers.add_parser(command.name)
        sub.set_defaults(func=command.run)
        for arg in command.arguments:
            sub.add_argument(arg)

    help_command = commands[0]
    parser.set_defaults(func=help_command.run)

    return parser


def main(args):
    check_shell_integration()

    context = Context()

    parser = make_parser(context.get_commands())
    cliargs = parser.parse_args(args)
    command_func = cliargs.func
    context.set_args(cliargs)

    try:
        command_func()
    except KeyboardInterrupt:
        print("Ok Bye!")


def cli():
    main(sys.argv[1:])
