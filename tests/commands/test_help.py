

def test_help(appfunc, capsys):
    appfunc(['help'])

    out, err = capsys.readouterr()
    assert 'List of available commands' in out
    assert 'de init' in out
    assert 'de cd' in out


def test_usage(appfunc, capsys):
    appfunc([])

    out, err = capsys.readouterr()
    assert 'List of available commands' in out
