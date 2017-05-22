
class Command(object):
    tasks = []
    arguments = []

    @property
    def name(self):
        return self.__class__.__name__.lower()

    def run(self, context):
        self._run_tasks(context)

    def _run_tasks(self, context):
        for task_class in self.tasks:
            task = task_class(context)
            if task.applies():
                task.run()
