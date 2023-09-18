.PHONY: up vssh halt reload destroy status addkey ssh remkey

HOST=192.168.56.10

up:
	vagrant up

vssh:
	vagrant ssh

halt:
	vagrant halt

reload:
	vagrant reload

destroy:
	vagrant destroy

status:
	vagrant status

addkey:
	ssh-add ../playbook/roles/user/files/id_ed25519

ssh:
	ssh -i ../playbook/roles/user/files/id_ed25519 takashi@$(HOST)

remkey:
	ssh-keygen -R $(HOST)
