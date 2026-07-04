SHELL = /bin/bash
.ONESHELL:

dev-venv:
	cd ./scripts && ./setup_dev_env.sh

bench:
	python -m benchmark.run_all

tests:
	poetry run pytest

ci:
	make tests
	make bench
	docstr_coverage --fail-under 90

docstr_coverage: ## Check docstring coverage using docstr_coverage
	docstr_coverage

docker-build:
	docker-compose build

docker-up:
	docker-compose up -d

lint:
	poetry run flake8
	poetry run docstringstyle
	poetry run isort .
	poetry run black .
	poetry run mypy .