import argparse
import os
import pkg_resources
import sys
from pathlib import Path

from devup import integration
from devup.lib.config import Config
from devup.lib.context import Context
from devup.lib.project import Project

from devup.commands.cd import Cd
from devup.commands.clone import Clone
from devup.commands.init import Init
from devup.commands.custom import Custom


def make_help(commands):
    def func(context):
        context.write_output('List of available commands:\n\n', 'info')
        for command in commands:
            args = [arg.upper() for arg in command.arguments]
            args = ' '.join([command.name] + args)
            context.write_output('  de %-24s' % args, 'command')
            context.write_output('   %s\n\n' % command.description, 'info')
    return func


def setup_parser_commands(parser, commands):
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


def setup_parser_version(parser):
    try:
        version = pkg_resources.get_distribution('devup').version
    except:
        version = 'unknown'

    parser.add_argument(
        '--version',
        action='version',
        version='%%(prog)s %s' % version,
    )


def make_commands(project):
    command_classes = [Init, Clone, Cd]
    commands = [c() for c in command_classes]
    for name in project.command_names:
        command = Custom(name)
        commands.append(command)
    return commands


def run(args):
    config = Config(os.environ.copy())
    project = Project(Path.cwd())
    commands = make_commands(project)

    parser = argparse.ArgumentParser(prog='de')
    setup_parser_commands(parser, commands)
    setup_parser_version(parser)

    parsed_args = parser.parse_args(args)
    command_func = parsed_args.func

    context = Context(parsed_args, config, project)
    command_func(context)


def cli(app_function=run):
    integration.check()
    try:
        app_function(sys.argv[1:])
    except KeyboardInterrupt:
        print("👋")
        return 1
