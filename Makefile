.PHONY: build pull run lint tests clean

build:
	docker-compose build

publish: build
	docker-compose push

pull:
	docker-compose pull

run: pull
	docker-compose up -d web

lint:
	pre-commit run --all-files

tests:
	docker-compose pull api
	docker-compose up -d api
	docker-compose exec api pytest tests

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
