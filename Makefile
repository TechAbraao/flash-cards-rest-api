.PHONY: help venv install start create-database

VENV_DIR = .venv
VENV_PYTHON = $(VENV_DIR)/bin/python
VENV_PIP = $(VENV_DIR)/bin/pip
VENV_FLASK = $(VENV_DIR)/bin/flask

help:
	@echo ""
	@echo " * Available commands:"
	@echo " * venv             -> Creates virtual environment (.venv)"
	@echo " * install          -> Installs dependencies from src/requirements.txt"
	@echo " * start            -> Starts the REST API (Python/Flask)"
	@echo " * create-database  -> Initializes the database"
	@echo ""

venv:
	python3 -m venv $(VENV_DIR)

install:
	$(VENV_PIP) install -r src/requirements.txt

start:
	cd src && ../$(VENV_FLASK) run

create-database:
	cd src && PYTHONPATH=. ../$(VENV_PYTHON) -c "from app.settings.database.init_db import init_db; init_db()"
