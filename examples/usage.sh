$ de init

$ de clone devup
$ de clone pior/devup
$ de clone ssh://hg@bitbucket.org/pior/awstools

$ de cd devup
#-> project will autocompletion

$ de up
#-> should bring the environment as near as possible to a working state
#-> install deps
#-> setup local config like git hooks
#-> run bootstrap operation (create db? pull docker images?)
#-> run db migrations (support for sqlalchemy, django, rails...?)
#-> tell if other operations are needed (install tricky dependency? run a setup command)

$ de test
#-> run test suite
#-> should be usable in CI as well (or all other envs)

$ de test tests/lib/test_some_specific_test.py
$ de test -s
#-> pass through additional args (only?) to first test command

$ de lint
#-> run linter(s)

$ de clean
#-> clean up files (is it possible to infer this?)

$ de reset
#-> reset persisted state (partially revert `de up`)
#-> drop database (test db? dev db?)
