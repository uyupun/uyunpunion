.PHONY: start reload restart stop status ps log

SERVICE_NAME = gunicorn.service

password ?= ""
define SUDO_WITH_PASS
if [ -z "$(password)" ]; then \
	sudo $1; \
else \
	echo $(password) | sudo -S $1; \
fi
endef

start:
	$(call SUDO_WITH_PASS,systemctl enable --now $(SERVICE_NAME))

reload:
	$(call SUDO_WITH_PASS,systemctl daemon-reload)

restart:
	$(call SUDO_WITH_PASS,systemctl restart --now $(SERVICE_NAME))

stop:
	sudo systemctl stop $(SERVICE_NAME)

status:
	sudo systemctl status $(SERVICE_NAME)

ps: port ?= 8080
ps:
	ps u -p `pgrep -d, gunicorn`
	lsof -i :$(port)

log:
	sudo journalctl -u $(SERVICE_NAME) --no-pager
