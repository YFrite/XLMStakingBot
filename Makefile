APPLICATION_NAME ?= xlm_staking

compose_start:
	docker-compose up -d

delete_container:
	docker stop xlm_staking
	docker rm xlm_staking
	docker rmi xlm_staking

dev_setup:
	pip3 install -r dev_requirements.txt

setup:
	pip3 install -r requirements.txt

run:
	python3 main.py