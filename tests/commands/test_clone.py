

def test_with_no_arg(appfunc, capsys):
    exitcode = appfunc(['clone'])

    assert exitcode == 2

    out, err = capsys.readouterr()
    assert 'arguments are required: repository' in err


def test_already_cloned(appfunc, capsys):
    appfunc(['clone', 'pior/devup'])

    out, err = capsys.readouterr()
    assert 'project already exists' in out


def test_cloning(appfunc, projects, commands):
    appfunc(['clone', 'pior/new_project'])

    assert len(commands) == 1
    args = [
        'git',
        'clone',
        'git@github.com:pior/new_project.git',
        projects.join('github.com', 'pior', 'new_project'),
    ]
    assert commands[0] == args


def test_change_dir(appfunc, projects, finalizers):
    appfunc(['clone', 'pior/new_project'])

    new_project_path = projects.join('github.com', 'pior', 'new_project')
    assert ['cd', new_project_path] in finalizers()
