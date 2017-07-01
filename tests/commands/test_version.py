

def test_version(app, assert_in_output):
    app(['--version'])

    assert_in_output('de ')
