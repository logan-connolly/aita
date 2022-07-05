.DEFAULT_GOAL=help

build: # Build images locally
	@docker-compose build $(service)

push: # Push images to docker registry
	@docker-compose push $(service)

pull: # Pull required docker images
	@docker-compose pull $(service)

run: # Start application containers
	@docker-compose up -d
	@echo "Sleeping for 5 seconds while DB migrates ..."
	@sleep 5

lint: # Check and format via pre-commit
	@pre-commit run --all-files

tests: # Launch services and test
	@docker-compose up -d api
	@echo "Sleeping for 5 seconds while DB migrates ..."
	@sleep 5
	@docker-compose exec api pytest tests/api/test_posts.py

clean: # Clean up cache files
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete

help: # Show this help
	@egrep -h '\s#\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
