

def test_version(app, capsys):
    app(['--version'])

    out, err = capsys.readouterr()
    assert 'de ' in out
    assert 'unknown' not in out
