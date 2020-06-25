.PHONY: help up start up-mongo up-redis status logs restart clean mongo

up:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build

start:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --detach --build

up-mongo:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml run --publish=127.0.0.1:27017:27017 mongodb

up-redis:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml run --publish=127.0.0.1:6379:6379 redis

status:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml ps

logs:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml logs --tail=100

restart:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml stop
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --detach --build

clean:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml down

mongo:
	docker exec -it github-scraper_mongodb-dev bash
