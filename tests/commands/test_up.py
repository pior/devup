
def test_missing_devup_yml(app, manifest, assert_in_output):
    app(['up'], expect_status=1)
    assert_in_output('Invalid devup.yml: missing section')


def test_missing_command_section(app, manifest, assert_in_output):
    manifest.write('')
    app(['up'], expect_status=1)
    assert_in_output('Invalid devup.yml: missing section')


def test_command_section_not_a_list(app, manifest, assert_in_output):
    manifest.write('up: garbage')
    app(['up'], expect_status=1)
    assert_in_output('Invalid devup.yml: "up" section must be a list')


def test_empty_command_section(app, manifest, assert_in_output):
    manifest.write('up: []')
    app(['up'], expect_status=1)
    assert_in_output('Invalid devup.yml: I didn\'t find anything to do!')


def test_custom_commands(app, manifest, project):
    manifest.write("""
        up:
        - run: echo one > output
        - run: echo two >> output
    """)
    app(['up'])
    output = project.join('output').read()
    assert output == 'one\ntwo\n'


def test_failing_command(app, manifest):
    manifest.write("""
        up:
        - run: exit 1
    """)
    app(['up'], expect_status=0)


def test_command_if_run(app, manifest, project):
    manifest.write("""
        up:
        - run: echo one > output
          if: exit 0
    """)
    app(['up'])
    assert project.join('output').check()
    assert 'one\n' == project.join('output').read()


def test_command_if_not_run(app, manifest, project):
    manifest.write("""
        up:
        - run: echo one > output
          if: exit 1
    """)
    app(['up'])
    assert not project.join('output').check()
