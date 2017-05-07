
class Command(object):
    def __init__(self, context):
        self._context = context

    @property
    def arguments(self):
        return {arg for task in self.tasks for arg in task.arguments}

    def run(self):
        self._run_tasks()

    def _run_tasks(self):
        for task_class in self.tasks:
            task = task_class(self._context)
            task()
