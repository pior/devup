import yaml


def test_devup_create_a_manifest(appfunc, manifest):
    appfunc(['init'])
    assert manifest.exists()


def test_devup_doesnt_overwrite(appfunc, manifest):
    manifest.write('foobar')
    appfunc(['init'])
    assert manifest.read() == 'foobar'


def test_devup_create_a_yaml_valid_manifest(appfunc, manifest):
    appfunc(['init'])
    content = manifest.read()
    yaml.safe_load(content)
