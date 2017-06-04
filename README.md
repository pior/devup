# DevUp

[![CircleCI](https://circleci.com/gh/pior/devup.svg?style=svg)](https://circleci.com/gh/pior/devup)
[![codecov](https://codecov.io/gh/pior/devup/branch/master/graph/badge.svg)](https://codecov.io/gh/pior/devup)

CLI tool to manage your development projects.

DevUp purpose is to let anyone easily start contributing to a project.

```shell
~$ de clone pior/buddy
🔍 githubclone: Cloning repository from github
🔍 githubclone: git clone git@github.com:pior/buddy.git /home/pior/src/github.com/pior/buddy
Cloning into '/home/pior/src/github.com/pior/buddy'...

~/src/github.com/pior/buddy (master)$ de up
🔍 python-requirement: Installing dependencies...
🔍 python-requirement: done
🔍 python-setuptools-dev: Installing local project in development...
🔍 python-setuptools-dev: done

~/src/github.com/pior/buddy (master)$ de test
🔍 tox: running...
...
```

Commands:

- `de clone`: Clone your project
- `de cd`: Go to your already cloned project
- `de init`: Create an empty `devup.yml`
- `de test`: Run your test suite (TODO)
- `de lint`: Run your linter (TODO)
- `de setup`: Configure your local devel environment (TODO)
- `de ci`: Run the CI test suite (TODO)
- `de mycommand`: Run custom commands defined by the project (TODO)

## What is this?

DevUp is a minimal re-implementation of an amazing internal tool developed at
Shopify.

## The project

At first DevUp commands will only be based on what devup.yml is declaring.

Then, automatic discovery will try to make command declaration optional as much as possible.

Still, DevUp will always stay transparent regarding its actions to help contributors understand the tools used by a project.

DevUp will be language agnostic. (although it may start a bit Python-centric since it's the language of choice of the initial author)
