#!/bin/sh

cd playbook
pipenv run ansible-lint site.yml
