.DEFAULT_GOAL=help

bootstrap: # Install dependencies via poetry
	pip install -r requirements/requirements.txt
	pip install -r requirements/dev-requirements.txt
	python -m spacy download en_core_web_sm

debugserver: # Launch debug uvicorn server locally
	ENV=debug PYTHONPATH=. ./start.sh

devserver: # Launch dev uvicorn server locally
	ENV=dev PYTHONPATH=. ./start.sh

prodserver: # Launch prod gunicorn server locally
	ENV= PYTHONPATH=. ./start.sh

pytest: # Run unittests tests
	pytest tests

mypy: # Run mypy static analysis tests
	mypy --ignore-missing-imports app

migration: # Make an autogenerated alembic migration
	PYTHONPATH=. alembic revision --autogenerate

clean: # Clean up cache files
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete

help: # Show this help
	@egrep -h '\s#\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
