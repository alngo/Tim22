MODULE := tim21

BLUE=\033[0;34m
NC=\033[0m # No Color

.PHONY: sh clean test build

run: build
	docker-compose --file docker/docker-compose.yml run tim22

sh: build
	docker-compose --file docker/docker-compose.yml run tim22_sh

build:
	docker-compose --file docker/docker-compose.yml up --no-start --remove-orphans

test:
	@coverage run --rcfile=.config/setup.cfg -m pytest
	@echo "\n$(BLUE)Coverage$(NC)\n"
	@coverage report -m
	@echo "\n$(BLUE)Security check$(NC)\n"
	@bandit -r --ini .config/setup.cfg

clean:
	rm -rf .pytest_cache .coverage .pytest_cache coverage.xml
