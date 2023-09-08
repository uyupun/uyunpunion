.PHONY: up reload down ps

up:
	pipenv run prod

reload:
	kill -HUP `cat gunicorn.pid`

down:
	kill `cat gunicorn.pid`

ps:
	ps u -p `pgrep -d, gunicorn`
