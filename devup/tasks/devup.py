import textwrap
from pathlib import Path

from devup.tasks import Task, TaskShouldNotRun


class Devup(Task):
    action_message = 'Creating an initial devup.yml'
    post_message = 'Open `devup.yml` and configure it for your project.'

    declaration = Path('devup.yml')
    content = """# File created by 'de init'

        up:

        test:
          # command: ./manage.py test
          # command: rails test
          # command: go test
    """

    def _should_run(self):
        if self.declaration.exists():
            return TaskShouldNotRun('A devup.yml file already exists')
        return True

    def _run(self):
        self.declaration.write_text(textwrap.dedent(self.content))
