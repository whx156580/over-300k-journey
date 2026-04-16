PYTHON ?= python
PORT ?= 8000

.PHONY: install serve test lint format check

install:
	$(PYTHON) -m pip install -r requirements.txt

serve:
	$(PYTHON) -m http.server $(PORT) -d .

test:
	$(PYTHON) -m pytest tests -q

lint:
	$(PYTHON) -m flake8 tests
	$(PYTHON) -m mypy tests

format:
	$(PYTHON) -m isort tests
	$(PYTHON) -m black tests

check: test lint
