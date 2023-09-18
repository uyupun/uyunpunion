.PHONY: chmod addkey encrypt decrypt ping ls check dryrun run

env ?= devel
tags ?= all

chmod:
	chmod 600 roles/user/files/id_ed25519

addkey:
	ssh-add roles/user/files/id_ed25519

encrypt:
	pipenv run ansible-vault encrypt roles/user/vars/main.yml

decrypt:
	pipenv run ansible-vault decrypt roles/user/vars/main.yml

ping:
	pipenv run ansible all -i inventories/$(env) -m ping

ls:
	pipenv run ansible-playbook -i inventories/$(env) site.yml --list-tasks

check:
	pipenv run ansible-playbook -i inventories/$(env) site.yml --syntax-check
	pipenv run ansible-lint site.yml

dryrun:
	pipenv run ansible-playbook -i inventories/$(env) site.yml --check --diff --tags $(tags)

run:
	pipenv run ansible-playbook -i inventories/$(env) site.yml --tags $(tags)
