import sys
import traceback

from devup.utils import output
from devup.lib import command


class TaskShouldNotRun(Exception):
    def __bool__(self):
        return False


class TaskError(Exception):
    pass


class TaskFailed(TaskError):
    pass


class TaskConfigError(TaskError):
    pass


class Task(object):
    """Base class for tasks.

    >>> task = MyTask(context)
    >>> print(task.name)
    >>> applies_to_context = task.applies()
    >>> task.run()
    """
    arguments = []
    action_message = False

    def __init__(self, context, config=None):
        self._context = context
        self._config = config

    @property
    def _arg(self, name=None):
        arg_name = self.arguments[0]
        return getattr(self._context.args, arg_name)

    @property
    def name(self):
        return output.humanize(self.__class__.__name__)

    @staticmethod
    def applies():
        """Whether this task applies to the current context."""
        return True

    @staticmethod
    def _should_run():
        """Whether this task needs to run for the current context."""
        return True

    @staticmethod
    def _run():
        """Task actual action implementation."""
        return True

    def _print(self, message, style):
        self._context.write_output('🔍 ', style='bold')
        self._context.write_output(self.name, style='header')
        self._context.write_output(': %s\n' % message, style=style)

    def _run_command(self, args):
        self._print(' '.join(args), 'command')
        return command.run(args)

    def _safe_run_command(self, args):
        try:
            return command.run(args)
        except command.Error as err:
            self._context.exit('command failed: %s' % err)

    def run(self):
        should_run = self._should_run()

        if not should_run:
            if isinstance(should_run, TaskShouldNotRun):
                message = should_run
            else:
                message = 'all good'
            self._print('%s ✔' % message, 'success')
            return

        if self.action_message:
            self._print(self.action_message, 'info')

        try:
            self._run()
        except TaskFailed as err:
            self._print(str(err), 'error')
        except TaskConfigError as err:
            self._print(
                "%s\nConfig section: %s" % (err, self._config),
                'error',
            )
        except Exception as err:
            self._crash(err)

        if hasattr(self, 'post_message'):
            self._print("➡ %s" % self.post_message, 'help')

    def _crash(self, err):
        exc_tb = sys.exc_info()[2]
        filename, line_num, func_name, _ = traceback.extract_tb(exc_tb)[-1]
        del exc_tb
        self._print('Crash: %s' % err, 'error')
        self._print(
            ' in %s (%s:%s)' % (func_name, filename, line_num),
            'error'
        )
        sys.exit(1)
