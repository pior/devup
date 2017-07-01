

def test_help(app, capsys):
    app(['help'])

    out, err = capsys.readouterr()
    assert 'List of available commands' in out
    assert 'de init' in out
    assert 'de cd' in out


def test_usage(app, capsys):
    app([])

    out, err = capsys.readouterr()
    assert 'List of available commands' in out
