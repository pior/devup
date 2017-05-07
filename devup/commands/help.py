from .base import Command


class Help(Command):
    name = 'help'
    tasks = []

    def _print(self, msg, style):
        self._context.write_output(msg, style)

    def run(self):
        self._print('List of available commands:\n\n', 'info')

        for command in self._context.get_commands():
            if command.name == 'help':
                continue
            self._print('➡️ ', 'header')
            self._print('$ de %-8s' % command.name, 'command')
            self._print('   %s\n\n' % command.description, 'info')
