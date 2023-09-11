.PHONY: start reload restart stop status ps log

SERVICE_NAME = gunicorn.service

start:
	sudo systemctl enable --now $(SERVICE_NAME)

reload:
	sudo systemctl daemon-reload

restart:
	sudo systemctl restart --now $(SERVICE_NAME)

stop:
	sudo systemctl stop $(SERVICE_NAME)

status:
	sudo systemctl status $(SERVICE_NAME) --no-pager

ps: port ?= 8080
ps:
	ps u -p `pgrep -d, gunicorn`
	lsof -i :$(port)

log:
	sudo journalctl -u $(SERVICE_NAME) --no-pager
