import yaml


def test_devup_create_a_manifest(app, manifest):
    app(['init'])
    assert manifest.exists()


def test_devup_doesnt_overwrite(app, manifest):
    manifest.write('foobar')
    app(['init'])
    assert manifest.read() == 'foobar'


def test_devup_create_a_yaml_valid_manifest(app, manifest):
    app(['init'])
    content = manifest.read()
    yaml.safe_load(content)
