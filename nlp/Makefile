.DEFAULT_GOAL=help

bootstrap: # Install dependencies
	pip install -r requirements/requirements.txt
	pip install -r requirements/dev-requirements.txt
	python -m spacy download en_core_web_sm

coverage: # Run unittests tests and calculate coverage
	coverage run -m pytest tests
	coverage report --skip-covered

mypy: # Run mypy static analysis tests
	mypy --ignore-missing-imports nlp

clean: # Clean up cache files
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete

help: # Show this help
	python -m nlp --help || true
	@echo
	@grep -E -h '\s#\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
