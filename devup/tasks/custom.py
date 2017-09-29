import os

from devup.tasks import Task
from devup.lib import command


class CustomCommand(Task):
    name = 'run'

    def _should_run(self):
        if 'if' in self._config:
            if_args = self._config['if']
            try:
                self._run_command(if_args)
            except command.NotFoundError as err:
                self._crash(err)
            except command.Failed:
                return False

        if 'if-env' in self._config:
            env = self._config['if-env']
            if env not in os.environ:
                return False

        return True

    def _run(self):
        run_args = self._config['run']
        try:
            self._run_command(run_args)
        except command.NotFoundError as err:
            self._crash(err)
        except command.Failed:
            pass
