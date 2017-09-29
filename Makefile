.PHONY: setup
setup:
	pip install -U pip
	pip install -e .
	pip install -r requirements-dev.txt

.PHONY: test
test:
	py.test

.PHONY: lint
lint:
	flake8 devup tests
