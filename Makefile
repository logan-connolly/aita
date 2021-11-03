.PHONY: build pull run lint tests clean

export_deps:
	cd api && poetry install && poetry export --without-hashes -o requirements.txt

build: export_deps
	docker-compose build $(service)

publish: build
	docker-compose push $(service)

pull:
	docker-compose pull $(service)

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
