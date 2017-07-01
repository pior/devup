
def test_with_no_arg(app, capsys):
    app(['clone'], expect_status=2)

    out, err = capsys.readouterr()
    assert 'arguments are required: repository' in err


def test_already_cloned(app, capsys):
    app(['clone', 'pior/devup'])

    out, err = capsys.readouterr()
    assert 'project already exists' in out


def test_cloning(app, projectsdir, commands):
    app(['clone', 'pior/new_project'])

    assert len(commands) == 1
    args = [
        'git',
        'clone',
        'git@github.com:pior/new_project.git',
        projectsdir.join('github.com', 'pior', 'new_project'),
    ]
    assert commands[0] == args


def test_change_dir(app, projectsdir, finalizers):
    app(['clone', 'pior/new_project'])

    new_project_path = projectsdir.join('github.com', 'pior', 'new_project')
    assert ['cd', new_project_path] in finalizers()
