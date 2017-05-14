import argparse
import sys

from . import integration
from .context import Context

from .commands.cd import Cd
from .commands.clone import Clone
from .commands.init import Init

command_classes = [Init, Clone, Cd]


def make_help(commands):
    def func(context):
        context.write_output('List of available commands:\n\n', 'info')
        for command in commands:
            context.write_output('  de %-8s' % command.name, 'command')
            context.write_output('   %s\n\n' % command.description, 'info')
    return func


def make_parser(commands):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    def add_command(name, func, args):
        sub = subparsers.add_parser(name)
        sub.set_defaults(func=func)
        for arg in args:
            sub.add_argument(arg)

    for cmd in commands:
        add_command(cmd.name, cmd.run, cmd.arguments)

    help_func = make_help(commands)
    add_command('help', help_func, [])
    parser.set_defaults(func=help_func)

    return parser


def main(args):
    try:
        integration.check()

        commands = [c() for c in command_classes]

        parser = make_parser(commands)
        parsed_args = parser.parse_args(args)
        command_func = parsed_args.func

        context = Context(parsed_args)
        command_func(context)
    except KeyboardInterrupt:
        print("👋")


def cli():
    main(sys.argv[1:])
