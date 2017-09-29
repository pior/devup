import pkg_resources

from devup.tasks import Task, TaskShouldNotRun


class Devup(Task):
    action_message = 'Creating an initial devup.yml'
    post_message = 'Open `devup.yml` and configure it for your project.'

    def _should_run(self):
        if self._context.project.manifest.exists():
            return TaskShouldNotRun('A devup.yml file already exists')
        return True

    def _run(self):
        content = pkg_resources.resource_string('devup', '/files/devup.yml')
        self._context.project.manifest.write_bytes(content)
