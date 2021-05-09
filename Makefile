.PHONY: build pull run lint tests clean

build:
	docker-compose build

pull:
	docker-compose pull

run: pull
	docker-compose up -d ui

lint:
	pre-commit run --all-files

tests:
	docker-compose pull api
	docker-compose up -d api
	docker-compose exec api pytest tests

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
