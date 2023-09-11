#!/bin/sh

cp .pre-commit-config.yaml ../.pre-commit-config.yaml
pipenv run pre-commit install
rm -rf ../.pre-commit-config.yaml
sed -i "s|--config=.pre-commit-config.yaml|--config=hooks/.pre-commit-config.yaml|" .git/hooks/pre-commit
