import pytest

from devup import app as devup_app
from devup.lib import command


@pytest.fixture()
def assert_in_output(capsys):
    def func(*substrings, stderr=False):
        out, err = capsys.readouterr()
        output = err if stderr else out
        for substring in substrings:
            assert substring in output
    return func


@pytest.fixture()
def app(monkeypatch, projectsdir, project, other_project):
    monkeypatch.chdir(project)
    monkeypatch.setenv('PROJECTS_PATH', str(projectsdir))

    def func(args, expect_status=0):
        try:
            devup_app.run(args)
        except SystemExit as exit:
            code = exit.code
        else:
            code = 0
        assert code == expect_status
    return func


@pytest.fixture()
def projectsdir(tmpdir):
    projectsdir = tmpdir  # Get one tmpdir and call it our projects directory
    return projectsdir


@pytest.fixture()
def project(projectsdir):
    projectdir = projectsdir.join('github.com', 'pior', 'devup')
    projectdir.ensure(dir=True)
    return projectdir


@pytest.fixture()
def other_project(projectsdir):
    projectdir = projectsdir.join('github.com', 'pior', 'other')
    projectdir.ensure(dir=True)
    return projectdir


@pytest.fixture()
def finalizers(tmpdir, monkeypatch):
    finalizer_file = tmpdir.join('finalizer')
    finalizer_file.ensure()
    monkeypatch.setenv('DEVUP_FINALIZER_FILE', str(finalizer_file))

    def func():
        return [line.strip().split(':') for line in finalizer_file.readlines()]
    return func


@pytest.fixture()
def manifest(project):
    devupyml = project.join('devup.yml')
    return devupyml


@pytest.fixture()
def commands(monkeypatch):
    calls = []

    def run(args):
        calls.append(args)
    monkeypatch.setattr(command, 'run', run)
    return calls
