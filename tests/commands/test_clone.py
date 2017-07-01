
def test_with_no_arg(app, assert_in_output):
    app(['clone'], expect_status=2)

    assert_in_output('arguments are required: repository', stderr=True)


def test_already_cloned(app, assert_in_output):
    app(['clone', 'pior/devup'])

    assert_in_output('project already exists')


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
