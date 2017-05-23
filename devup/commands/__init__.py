
class Command(object):
    arguments = []

    @property
    def name(self):
        return self.__class__.__name__.lower()

    def run(self, context):
        tasks = self._prepare_tasks(context)
        for task in tasks:
            if task.applies():
                task.run()

    def _prepare_tasks(self, context):
        return [task(context) for task in self._tasks]
