from devup.commands import ConfigError
from devup.tasks.python import SetuptoolsDevelop, PipRequirements
from devup.tasks.custom import CustomCommand


TASKS = [SetuptoolsDevelop, PipRequirements, CustomCommand]
TASKS_MAP = {t.name: t for t in TASKS}


def find_task_name(item):
    # without config, eg:
    # - setuptools_develop
    if isinstance(item, str):
        return item

    # with config, eg:
    # - run: ./run-integration-test.sh
    #   if-env: CI
    if isinstance(item, dict):
        for key in list(item.keys()):
            if key in TASKS_MAP:
                return key


def build(context, item):
    task_name = find_task_name(item)

    if not task_name:
        raise ConfigError('invalid section: %s' % item)

    task_class = TASKS_MAP.get(task_name)
    if not task_class:
        raise ConfigError('unknown task: %s' % task_name)

    return task_class(context, item)
