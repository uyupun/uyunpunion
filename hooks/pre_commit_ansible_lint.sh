#!/bin/sh

cd hooks
export ANSIBLE_CONFIG=../playbook/ansible.cfg
pipenv run ansible-lint ../playbook/site.yml
