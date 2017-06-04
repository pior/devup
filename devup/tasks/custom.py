from devup.tasks import Task, TaskConfigError
from devup.lib import command


def parse_config(config):
    should_run_args = None

    if isinstance(config, str):
        run_args = config.split()
    elif isinstance(config, dict):
        if 'command' not in config:
            raise TaskConfigError("Missing 'command' key")
        run_args = config['command'].split()
    else:
        raise TaskConfigError("Invalid task config")

    return run_args, should_run_args


class CustomCommand(Task):
    name = 'custom'

    def _should_run(self):
        _, should_run_args = parse_config(self._config)
        if not should_run_args:
            return True
        try:
            self._run_command(should_run_args)
        except command.NotFoundError as err:
            self._crash(err)
        else:
            return True

    def _run(self):
        run_args, _ = parse_config(self._config)
        try:
            self._run_command(run_args)
        except command.NotFoundError as err:
            self._crash(err)
