.PHONY: start restart stop ps

start:
	pipenv run prod

restart:
	kill -HUP `cat gunicorn.pid`

stop:
	kill `cat gunicorn.pid`

ps: port ?= 8080
ps:
	ps u -p `pgrep -d, gunicorn`
	lsof -i :$(port)
