import argparse
import os
import sys

from devup import integration
from devup.lib.config import Config
from devup.lib.context import Context

from devup.commands.cd import Cd
from devup.commands.clone import Clone
from devup.commands.init import Init
from devup.commands.up import Up

command_classes = [Init, Clone, Cd, Up]


def make_help(commands):
    def func(context):
        context.write_output('List of available commands:\n\n', 'info')
        for command in commands:
            args = [arg.upper() for arg in command.arguments]
            args = ' '.join([command.name] + args)
            context.write_output('  de %-24s' % args, 'command')
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


def run(args, env):
    commands = [c() for c in command_classes]

    parser = make_parser(commands)
    parsed_args = parser.parse_args(args)
    command_func = parsed_args.func

    config = Config(env)
    context = Context(parsed_args, config)
    command_func(context)


def cli(app_function=run):
    integration.check()
    try:
        app_function(sys.argv[1:], os.environ.copy())
    except KeyboardInterrupt:
        print("👋")
        return 1
