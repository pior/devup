from devup import app


def test_help(capsys):
    app.run(['help'], {})
    out, err = capsys.readouterr()
    assert 'List of available commands' in out
    assert 'de init' in out
    assert 'de cd' in out


def test_usage(capsys):
    app.run([], {})
    out, err = capsys.readouterr()
    assert 'List of available commands' in out
