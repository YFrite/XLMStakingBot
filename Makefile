APPLICATION_NAME ?= xlm_staking

build:
	docker build --tag xlm_staking ./

compose_start:
	docker-compose up -d

dev:
	pip install -r dev-requiremets.txt

run:
	python main.py