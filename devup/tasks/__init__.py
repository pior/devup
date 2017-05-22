import sys
import traceback
from subprocess import CalledProcessError

from devup.utils import output


class TaskShouldNotRun(Exception):
    def __bool__(self):
        return False


class TaskFailed(Exception):
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

    def __init__(self, context):
        self._context = context

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
        try:
            self._context.run_command(args)
        except CalledProcessError as err:
            msg = 'command failed with error %s' % err.returncode
            self._context.panic(msg)

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
        except Exception as err:
            exc_tb = sys.exc_info()[2]
            filename, line_num, func_name, _ = traceback.extract_tb(exc_tb)[-1]
            del exc_tb
            self._print('Crash: %s' % err, 'error')
            self._print(
                ' in %s (%s:%s)' % (func_name, filename, line_num),
                'error'
            )

        if hasattr(self, 'post_message'):
            self._print("➡ %s" % self.post_message, 'help')
