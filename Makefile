STAGED_FILES = $(shell git diff --name-only --diff-filter=d --staged | grep -E '\.py$$' | tr '\n' ' ')
ifneq ($(files),)
	FILES = $(files)
else ifneq ($(STAGED_FILES),)
	FILES = $(STAGED_FILES)
else
	FILES = ./blog_project
endif

install:
	poetry install
	poetry run pre-commit install

lint:
    poetry run flake8 --config=setup.cfg $(FILES)

format:
	poetry run black $(FILES)
	poetry run isort $(FILES)

typecheck:
	poetry run mypy blog_project --config-file=setup.cfg --namespace-packages --explicit-package-bases
