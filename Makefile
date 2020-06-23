MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.ONESHELL:
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:

SOURCE_DIR := src
TEST_DIR := tests

.PHONY: help
help:  ## print help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

## dependencies

.PHONY: deps-update
deps-update:
	pip install --upgrade pip pip-tools
	pip-compile --upgrade --output-file requirements/main.txt requirements/main.in
	pip-compile --upgrade --output-file requirements/dev.txt requirements/dev.in

.PHONY: deps-sync
deps-sync:
	pip-sync requirements/main.txt requirements/dev.txt

.PHONY: deps-update-sync
deps-update-sync: deps-update deps-sync

.PHONY: deps-install
deps-install:  ## install dependencies
	pip install --upgrade pip
	pip install -r requirements/main.txt -r requirements/dev.txt

## checks

.PHONY: format
format:
	black $(SOURCE_DIR) $(TEST_DIR)

.PHONY: lint
lint:
	black $(SOURCE_DIR) $(TEST_DIR) --diff
#	isort --check-only
#	flake8 $(SOURCE_DIR) $(TEST_DIR)
#	mypy $(SOURCE_DIR)

.PHONY: test
test:
	pytest $(TEST_DIR) --cov $(SOURCE_DIR)

.PHONY: run-ci
run-ci: deps-install lint test  ## run ci
