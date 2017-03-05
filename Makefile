VIRTUAL_ENV?=.venv
PYTHON?=$(VIRTUAL_ENV)/bin/python
PIP?=$(VIRTUAL_ENV)/bin/pip
COVERAGE?=$(VIRTUAL_ENV)/bin/coverage
FALKE8?=$(VIRTUAL_ENV)/bin/flake8
ISORT?=$(VIRTUAL_ENV)/bin/isort
WATCHMEDO=$(VIRTUAL_ENV)/bin/watchmedo
BROWSER?=firefox
PACKAGE?=chordchart_notation

help:
	@## Displays this message
	@echo -e "Usage:\n"
	@awk ' \
		/^[a-zA-Z_-]+:/ { \
			t = $$0; \
			sub(/:.*/, "", t) \
		} \
		/^\s+@?##/ { \
			h = $$0; \
			sub(/^\s*@*##/, "", h); \
			print "\t" t "\t" h; \
			t = "" \
		} \
	' Makefile | column -t -s $$'\t'

venv: $(PYTHON)
$(PYTHON):
	python -m venv $(VIRTUAL_ENV)

testing-requirements: venv
	$(PIP) install ".[testing]"

develop-requirements: venv
	$(PIP) install -e ".[develop]"

develop: testing-requirements develop-requirements
	@## Install in developpent mode
	$(PYTHON) setup.py develop

typecheck:
	@## Run the tests
	$(PYTHON) -m mypy $(PACKAGE)

test:
	@## Run the tests
	$(PYTHON) -m unittest

lint:
	@## Run lint tests
	$(FALKE8) $(PACKAGE) tests

watch: COMMAND = $(MAKE) $(filter-out watch, $(MAKECMDGOALS))
watch:
	@## Run command on source changes
	$(WATCHMEDO) shell-command -R -W -p '*.py' -c '$(COMMAND)'

isort:
	@## Sort python imports
	$(ISORT) --recursive $(PACKAGE) tests setup.py

coverage:
	@## Show coverage in the console
	$(COVERAGE) run -m unittest
	$(COVERAGE) report -m

coverage-html:
	@## Show coverage in the browser
	$(COVERAGE) run -m unittest
	$(COVERAGE) html
	$(BROWSER) htmlcov/index.html

clean-coverage:
	@## Remove coverage files
	rm -rf .coverage htmlcov

clean-pyc:
	@## Remove python cache files
	find -name '__pycache__' | xargs rm -rf {}
	find -name '*.pyc' -exec rm -f {} \;

clean: clean-coverage  clean-pyc
	@## Remove intermediate files
	rm -rf *.egg-info
