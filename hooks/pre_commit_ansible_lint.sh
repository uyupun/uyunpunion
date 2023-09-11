#!/bin/sh

export ANSIBLE_CONFIG=../playbook/ansible.cfg
cd hooks
pipenv run ansible-lint ../playbook/site.yml
