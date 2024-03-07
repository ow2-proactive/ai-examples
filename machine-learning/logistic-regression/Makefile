.PHONY: virtualenv help

virtualenv:
	rm -rf env
	python3 -m venv env
	. env/bin/activate && python3 -m pip install --upgrade pip setuptools twine
	. env/bin/activate && python3 -m pip install -r requirements.txt
	. env/bin/activate && python3 -m pip -V

help:
	cat Makefile
