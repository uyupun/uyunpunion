.PHONY: up reload down ps

up:
	pipenv run prod

reload:
	kill -HUP `cat gunicorn.pid`

down:
	kill `cat gunicorn.pid`

ps: port ?= 8080
ps:
	ps u -p `pgrep -d, gunicorn`
	lsof -i :$(port)
