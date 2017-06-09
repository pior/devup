

def test_with_no_arg(appfunc, capsys):
    exitcode = appfunc(['cd'])
    assert exitcode == 2

    out, err = capsys.readouterr()
    assert 'arguments are required: project' in err


def test_with_unknown_project(appfunc, capsys, projects):
    env = {'PROJECTS_PATH': projects}
    appfunc(['cd', 'nope'], env)

    out, err = capsys.readouterr()
    assert 'Unknown project nope' in out


def test_finalizer(appfunc, projects, project, finalizers):
    env = {'PROJECTS_PATH': projects}
    appfunc(['cd', 'devup'], env)

    assert ['cd', str(project)] in finalizers()
