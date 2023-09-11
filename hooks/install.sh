#!/bin/sh

chmod +x pre_commit_ansible_lint.sh

cp .pre-commit-config.yml .pre-commit-config.yaml
pipenv run pre-commit install
perl -pi -e "s|--config=hooks/.pre-commit-config.yaml|--config=hooks/.pre-commit-config.yml|" ../.git/hooks/pre-commit
rm -rf .pre-commit-config.yaml
