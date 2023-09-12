.PHONY: nw start restart stop log shell

nw:
	docker network create --driver bridge --subnet 172.20.0.0/16 uyunpunion-network

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
