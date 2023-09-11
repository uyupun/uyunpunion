#!/bin/sh

chmod +x pre_commit_ansible_lint.sh

cp .pre-commit-config.yaml ../.pre-commit-config.yaml
pipenv run pre-commit install
rm -rf ../.pre-commit-config.yaml
sed -i "s|--config=.pre-commit-config.yaml|--config=hooks/.pre-commit-config.yml|" .git/hooks/pre-commit
