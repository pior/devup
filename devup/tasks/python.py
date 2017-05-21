from . import Task


class SetuptoolsDevelop(Task):
    def applies(self):
        return self._context.project.path.joinpath('setup.py').exists()

    def run(self):
        self._run_command(['pip', 'install', '-e', '.'])
