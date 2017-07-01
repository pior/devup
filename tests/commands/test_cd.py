
def test_with_no_arg(app, capsys):
    app(['cd'], expect_status=2)

    out, err = capsys.readouterr()
    assert 'arguments are required: project' in err


def test_with_unknown_project(app, capsys):
    app(['cd', 'nope'])

    out, err = capsys.readouterr()
    assert 'Unknown project nope' in out


def test_finalizer(app, project, finalizers):
    app(['cd', 'devup'])

    assert ['cd', str(project)] in finalizers()
