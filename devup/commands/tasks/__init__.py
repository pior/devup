from subprocess import CalledProcessError


class TaskResponse(object):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class TaskShoudNotRun(TaskResponse):
    pass


class Task(object):
    arguments = []
    action_message = 'running'

    def __init__(self, context):
        self._context = context
        self._init()

    def _init(self):
        pass

    @property
    def _arg(self, name=None):
        arg_name = self.arguments[0]
        return getattr(self._context.args, arg_name)

    @property
    def name(self):
        return self.__class__.__name__.lower()

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

    def __call__(self):
        response = self.should_run()

        if isinstance(response, TaskShoudNotRun):
            self._print('%s ✔️' % response, 'success')
        elif response is False:
            self._print('all good ✔️', 'success')
        else:
            self._print(self.action_message, 'info')
            self.run()
            self._print("Success ✔️", 'success')

            if hasattr(self, 'post_message'):
                self._print("➡️ %s" % self.post_message, 'help')
