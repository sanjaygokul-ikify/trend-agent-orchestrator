all: build

build:
	poetry build

dev:
	poetry run python -m agent_orchestrator

test:
	poetry run pytest