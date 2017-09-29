
def test_with_no_arg(app, assert_in_output):
    app(['cd'], expect_status=2)

    assert_in_output('arguments are required: project', stderr=True)


def test_with_unknown_project(app, assert_in_output):
    app(['cd', 'nope'])

    assert_in_output('Unknown project nope')


def test_finalizer(app, project, finalizers):
    app(['cd', 'devup'])

    assert ['cd', str(project)] in finalizers()
