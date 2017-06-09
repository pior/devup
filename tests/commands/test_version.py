

def test_version(appfunc, capsys):
    exit_code = appfunc(['--version'])

    assert exit_code == 0

    out, err = capsys.readouterr()
    assert 'de ' in out
    assert 'unknown' not in out
