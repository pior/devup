from devup.tasks import Task


class SetuptoolsDevelop(Task):
    def applies(self):
        return self._context.project.path.joinpath('setup.py').exists()

    def run(self):
        self._run_command(['pip', 'install', '-e', '.'])


def find_requirements_file(path):
    devreq = list(path.glob('requirements*dev*.txt'))
    devreq += list(path.glob('dev*requirements.txt'))
    devreq += list(path.glob('requirements*/*dev*.txt'))
    if devreq:
        return devreq[0]

    reqfile = path.joinpath('requirements.txt')
    if reqfile.exists():
        return reqfile


class PipRequirements(Task):
    @property
    def requirements_file(self):
        path = find_requirements_file(self._context.project.path)
        if path:
            relative_path = path.relative_to(path.cwd())
            return str(relative_path)

    def applies(self):
        return bool(self.requirements_file)

    def run(self):
        self._run_command(['pip', 'install', '-r', self.requirements_file])
