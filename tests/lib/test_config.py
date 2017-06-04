import os

from devup.lib import config


def test_project_path_default():
    c = config.Config({})
    expected = os.path.expanduser('~/src')
    assert expected == str(c.projects_path)


def test_project_path_from_env():
    c = config.Config({'PROJECTS_PATH': '/src'})
    assert '/src' == str(c.projects_path)
