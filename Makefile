APPLICATION_NAME ?= xlm_staking

build:
	docker build --tag xlm_staking ./

compose_start:
	docker-compose up -d

run:
	python -m main.py