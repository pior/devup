from devup.commands import Command, ConfigError
from devup.commands import tasks


class Up(Command):
    name = 'up'
    description = 'Setup and maintain your development environment'

    def _prepare_tasks(self, context):
        command_config = context.project.get_command_config('up')

        if command_config is None:
            raise ConfigError('missing section "up"')
        elif not isinstance(command_config, list):
            raise ConfigError('"up" section must be a list')

        return [tasks.build(context, item) for item in command_config]
