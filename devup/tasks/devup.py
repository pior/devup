import textwrap
from pathlib import Path

from . import Task, TaskShouldNotRun


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

    def get_content(self):
        return textwrap.dedent(self.content)

    def should_run(self):
        if self.declaration.exists():
            return TaskShouldNotRun('A devup.yml file already exists')
        return True

    def run(self):
        self.declaration.write_text(self.get_content())
