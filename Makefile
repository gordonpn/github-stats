.DEFAULT_GOAL := help
.PHONY: help up start up-mongo up-redis status logs restart clean mongo init-db clean-db

up: ## Bring up dev stack with docker compose
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build

start: ## Bring up dev stack with docker compose, detached
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --detach --build

up-mongo: ## Bring up mongodb only
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml run --rm --publish=127.0.0.1:27017:27017 mongodb

status: ## Check stack status
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml ps

logs: ## Check stack logs
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml logs --tail=100

restart: ## Restart stack
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml stop
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --detach --build

clean: ## Bring down dev stack
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml down

mongo: ## Exec mongodb
	docker exec -it github-scraper_mongodb-dev bash

init-db: ## Run the init scripts for mongodb
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml run --rm --publish=127.0.0.1:27017:27017 mongodb

clean-db: ## Delete dev db volume and recreate it
	docker volume rm dev-mongodb-github-stats
	docker volume create --name=dev-mongodb-github-stats

help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sed -n 's/^\(.*\): \(.*\)##\(.*\)/\1\3/p' | column -t  -s ' '
