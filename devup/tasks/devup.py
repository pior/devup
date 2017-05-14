import os
import textwrap

from . import Task, TaskShouldNotRun


class Devup(Task):
    action_message = 'Creating an initial devup.yml'
    post_message = 'Open `devup.yml` and configure it for your project.'

    filename = 'devup.yml'
    content = """
        # File created by 'de init'

        test:
          # command: ./manage.py test
          # command: rails test
          # command: go test
    """

    def get_content(self):
        return bytes(textwrap.dedent(self.content), 'utf-8')

    def should_run(self):
        if os.path.exists(self.filename):
            return TaskShouldNotRun('A devup.yml file already exists')
        return True

    def run(self):
        with open(self.filename, 'wb') as fh:
            fh.write(self.get_content())
