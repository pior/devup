from devup.commands import Command, ConfigError
from devup.commands import tasks


class Custom(Command):
    description = 'Custom command declared in devup.yml'

    def __init__(self, name):
        self.name = name

    def _prepare_tasks(self, context):
        command_config = context.project.get_command_config(self.name)

        if command_config is None:
            raise ConfigError('missing section "%s"' % self.name)
        if not isinstance(command_config, list):
            raise ConfigError('"%s" section must be a list' % self.name)

        return [tasks.build(context, item) for item in command_config]
