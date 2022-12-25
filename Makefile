APPLICATION_NAME ?= xlm_staking

build:
	docker build --tag xlm_staking ./

run:
	python main.py