def test_version(run, capsys):
    exit_code = run(['--version'])

    assert exit_code == 0

    out, err = capsys.readouterr()
    assert 'de ' in out
    assert 'unknown' not in out
