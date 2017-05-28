
class Command(object):
    arguments = []

    @property
    def name(self):
        return self.__class__.__name__.lower()

    def run(self, context):
        tasks = self._prepare_tasks(context)

        if not tasks:
            context.write_output(
                "I didn't find anything to do! 😱\n"
                "You may want to edit your devup.yml file...",
                style='error',
            )
            return

        for task in tasks:
            if task.applies():
                task.run()

    def _prepare_tasks(self, context):
        return [task(context) for task in self._tasks]
