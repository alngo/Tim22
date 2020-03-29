MODULE := tim22

BLUE=\033[0;34m
NC=\033[0m # No Color

.PHONY: run watch test sh build rebuild all_tests re clean

run: build
	docker-compose --file docker/docker-compose.dev.yml run $(MODULE)

sh: build
	docker-compose --file docker/docker-compose.dev.yml run $(MODULE)_sh

watch: build
	docker-compose --file docker/docker-compose.dev.yml run $(MODULE)_watch

test: build
	docker-compose --file docker/docker-compose.dev.yml run $(MODULE)_test

build:
	docker-compose --file docker/docker-compose.dev.yml up --no-start --remove-orphans

rebuild:
	docker-compose --file docker/docker-compose.dev.yml up --build --no-start --remove-orphans

all_tests:
	@echo "\n$(BLUE)Pytest$(NC)\n"
	@coverage run --rcfile=.config/setup.cfg -m pytest
	@echo "\n$(BLUE)Coverage$(NC)\n"
	@coverage report --rcfile=.config/setup.cfg -m
	@echo "\n$(BLUE)Security check$(NC)\n"
	@bandit -r --ini .config/setup.cfg

re: clean
	rebuild

clean:
	rm -rf .pytest_cache .coverage .pytest_cache coverage.xml
