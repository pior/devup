import pytest

from devup import app


def test_with_no_arg(capsys):
    with pytest.raises(SystemExit) as exc:
        app.run(['clone'], {})
    assert exc.value.code == 2
    out, err = capsys.readouterr()
    assert 'arguments are required: repository' in err


def test_already_cloned(testenv, capsys):
    app.run(['clone', 'pior/devup'], testenv)
    out, err = capsys.readouterr()
    assert 'project already exists' in out


def test_cloning(testenv, projects, commands):
    app.run(['clone', 'pior/new_project'], testenv)

    assert len(commands) == 1
    args = [
        'git',
        'clone',
        'git@github.com:pior/new_project.git',
        projects.join('github.com', 'pior', 'new_project'),
    ]
    assert commands[0] == args


def test_change_dir(testenv, projects, commands, finalizers):
    app.run(['clone', 'pior/new_project'], testenv)

    new_project_path = projects.join('github.com', 'pior', 'new_project')
    assert ['cd', new_project_path] in finalizers()
