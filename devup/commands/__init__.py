
class Command(object):
    tasks = []

    @property
    def name(self):
        return self.__class__.__name__.lower()

    @property
    def arguments(self):
        return {arg for task in self.tasks for arg in task.arguments}

    def run(self, context):
        self._run_tasks(context)

    def _run_tasks(self, context):
        for task_class in self.tasks:
            task = task_class(context)
            if task.applies():
                task.run()
