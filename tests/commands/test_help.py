

def test_help(app, assert_in_output):
    app(['help'])

    assert_in_output('List of available commands', 'de init', 'de cd')


def test_usage(app, assert_in_output):
    app([])

    assert_in_output('List of available commands')
