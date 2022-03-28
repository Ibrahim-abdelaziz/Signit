# -*- Makefile -*-
SHELL=/bin/bash

# constants
PROJECT_NAME=Signit Service
BIND_TO=0.0.0.0
BIND_PORT=5050
FLASK=flask

.PHONY: run pip test shell clean clean-test clean-pyc lint
.DEFAULT_GOAL := run

run:
	@echo Starting $(PROJECT_NAME)...
	$(FLASK) run --host=$(BIND_TO) --port=$(BIND_PORT)

pip:
	pip install -r requirements/base.txt

test:
	pytest -svv

shell:
	@echo Open shell...
	$(FLASK) shell

clean: clean-pyc clean-test ## remove all test's stuff, coverage and Python artifacts

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with pylint
	pylint signit tests
