.PHONY: run

run:
	cd src && flask run --debug --host=0.0.0.0 --port=4000
