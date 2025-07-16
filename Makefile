.PHONY: run

run:
	cd src && flask run

create-db:
	PYTHONPATH=src python -c "from app.settings.database.init_db import init_db; init_db()"
