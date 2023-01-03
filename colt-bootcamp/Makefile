.PHONY: test format clean

venv: venv/touchfile

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

test: venv
	. venv/bin/activate; pytest

test-v: venv
	. venv/bin/activate; pytest -vv

format: venv
	. venv/bin/activate; isort . && black .

ft: format test

clean:
	rm -rf venv
