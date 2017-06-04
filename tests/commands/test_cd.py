import pytest

from devup import app


def test_with_no_arg(capsys):
    with pytest.raises(SystemExit) as exc:
        app.run(['cd'], {})
    assert exc.value.code == 2
    out, err = capsys.readouterr()
    assert 'arguments are required: project' in err


def test_with_unknown_project(capsys, projects):
    env = {'PROJECTS_PATH': projects}
    app.run(['cd', 'nope'], env)
    out, err = capsys.readouterr()
    assert 'Unknown project nope' in out


def test_finalizer(projects, project, finalizers):
    env = {'PROJECTS_PATH': projects}
    app.run(['cd', 'devup'], env)
    assert ['cd', str(project)] in finalizers()
