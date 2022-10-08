# 本番環境用のコマンド集

.PHONY: up reload down ps

up:
# localhost:8080で起動する場合は `--bind` オプションの指定は必要
# ポートのみを指定する場合は `--bind :8081`
# IPとポートを指定する場合は `--bind 0.0.0.0:8081` (0.0.0.0の場合はプライベートIPでのアクセスが可能となる)
	pipenv run prod

reload:
	kill -HUP `cat gunicorn.pid`

down:
	kill `cat gunicorn.pid`

ps:
	ps aux | grep gunicorn
