
class Error(Exception):
    pass


class ConfigError(Error):
    pass


class Command(object):
    arguments = []

    def run(self, context):
        try:
            tasks = self._prepare_tasks(context)

            if not tasks:
                raise ConfigError(
                    "I didn't find anything to do! 😱\n"
                    "You may want to edit your devup.yml file...",
                )

            for task in tasks:
                if task.applies():
                    task.run()
        except ConfigError as err:
            context.exit("Invalid devup.yml: %s" % err)

    def _prepare_tasks(self, context):
        return [task(context) for task in self._tasks]
