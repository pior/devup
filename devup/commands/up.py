from devup.commands import Command, ConfigError
from devup.tasks.python import SetuptoolsDevelop, PipRequirements
from devup.tasks.custom import CustomCommand


TASKS = [SetuptoolsDevelop, PipRequirements, CustomCommand]
TASKS_MAP = {t.name: t for t in TASKS}


class Up(Command):
    name = 'up'
    description = 'Setup and maintain your development environment'
    _tasks = [SetuptoolsDevelop, PipRequirements]

    def _prepare_tasks(self, context):
        section_content = context.project.config.get('up')
        if not isinstance(section_content, list):
            context.exit('Malformed devup.yml: "up" section must be a list')
        return [self._build_task(context, item) for item in section_content]

    def _build_task(self, context, item):
        config = None
        if isinstance(item, str):  # without config
            task_name = item
        elif isinstance(item, dict):  # with config
            if len(item) == 1:
                task_name, config = list(item.items())[0]
            else:
                raise ConfigError('invalid section "up": "%s"' % item)
        else:
            raise ConfigError('invalid section "up"')

        task_class = TASKS_MAP.get(task_name)
        if not task_class:
            raise ConfigError('unknown task: %s' % task_name)

        return task_class(context, config)
