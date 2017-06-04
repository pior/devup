import pytest

from devup.lib import command


@pytest.fixture()
def projects(tmpdir):
    projectdir = tmpdir
    projectdir.join('github.com', 'pior', 'project1').ensure(dir=True)
    projectdir.join('github.com', 'pior', 'devup').ensure(dir=True)
    return projectdir


@pytest.fixture()
def project(projects):
    return projects.join('github.com', 'pior', 'devup')


@pytest.fixture()
def testenv(projects, finalizers):
    return {'PROJECTS_PATH': projects}


@pytest.fixture()
def finalizers(tmpdir, monkeypatch):
    finalizer_file = tmpdir.join('finalizer')
    finalizer_file.ensure()
    monkeypatch.setenv('DEVUP_FINALIZER_FILE', str(finalizer_file))

    def func():
        return [line.strip().split(':') for line in finalizer_file.readlines()]
    return func


@pytest.fixture()
def manifest(project, monkeypatch):
    monkeypatch.chdir(project)
    devupyml = project.join('devup.yml')
    return devupyml


@pytest.fixture()
def commands(monkeypatch):
    calls = []

    def run(args):
        calls.append(args)
    monkeypatch.setattr(command, 'run', run)
    return calls
