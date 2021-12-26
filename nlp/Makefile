.DEFAULT_GOAL=help

bootstrap: # Install dependencies via poetry
	poetry install
	poetry run python -m spacy download en_core_web_sm

coverage: # Run unittests tests and calculate coverage
	poetry run coverage run -m pytest tests
	poetry run coverage report --skip-covered
	poetry run mypy nlp

mypy: # Run mypy static analysis tests
	poetry run mypy --ignore-missing-imports app

clean: # Clean up cache files
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete

help: # Show this help
	@egrep -h '\s#\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
