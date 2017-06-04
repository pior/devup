import yaml

from devup import app


def test_devup_create_a_manifest(manifest):
    app.run(['init'], {})
    assert manifest.exists()


def test_devup_doesnt_overwrite(manifest):
    manifest.write('foobar')
    app.run(['init'], {})
    assert manifest.read() == 'foobar'


def test_devup_create_a_yaml_valid_manifest(manifest):
    app.run(['init'], {})
    content = manifest.read()
    yaml.safe_load(content)
