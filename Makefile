MODULE := tim21

BLUE=\033[0;34m
NC=\033[0m # No Color

.PHONY: run sh build rebuild test re clean

run: build
	docker-compose --file docker/docker-compose.yml run $(MODULE)

sh: build
	docker-compose --file docker/docker-compose.yml run $(MODULE)_sh

build:
	docker-compose --file docker/docker-compose.yml up --no-start --remove-orphans

rebuild:
	docker-compose --file docker/docker-compose.yml up --build --no-start --remove-orphans

test:
	@coverage run --rcfile=.config/setup.cfg -m pytest
	@echo "\n$(BLUE)Coverage$(NC)\n"
	@coverage report -m --rcfile=.config/setup.cfg
	@echo "\n$(BLUE)Security check$(NC)\n"
	@bandit -r --ini .config/setup.cfg

re: clean
	rebuild

clean:
	rm -rf .pytest_cache .coverage .pytest_cache coverage.xml
