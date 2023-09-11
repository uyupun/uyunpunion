.PHONY: start restart stop log shell

start:
	docker compose up -d

restart:
	docker compose restart

stop:
	docker compose down

ps:
	docker compose ps

log:
	docker compose logs

shell:
	docker compose exec traefik sh
