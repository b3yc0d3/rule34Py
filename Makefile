# Extract the project name and version from the pyproject.toml file.
PROJECT = $(shell $(PYTHON3) scripts/read_pyproject.py project/name | tr 'A-Z' 'a-z')
VERSION = $(shell $(PYTHON3) scripts/read_pyproject.py project/version)

# Binaries
POETRY ?= poetry $(POETRY_ARGS)
POETRY_ARGS ?=
PYTHON3 ?= $(POETRY) run python3

PYTEST = $(POETRY) run pytest $(PYTEST_ARGS)
PYTEST_ARGS ?=
RUFF = $(POETRY) run ruff
SPHINX_BUILD = $(POETRY) run sphinx-build

# Source files
builddir ?= build
srcdir = rule34Py

dist_files = \
	$(srcdir) \
	LICENSE \
	NOTICE.md \
	pyproject.toml \
	README.md \

sdist = $(builddir)/$(PROJECT)-$(VERSION).tar.gz  # The python sdist.
wheels = $(builddir)/$(PROJECT)-$(VERSION)-py3-none-any.whl  # The python wheels.

# Installation Directories
prefix ?= /usr/local

docdir ?= $(prefix)/share/doc/$(project)
htmldir ?= $(docdir)/html


.DEFAULT_GOAL = all


# REAL TARGETS #
################

$(wheels) &: $(dist_files)
	$(POETRY) build --output $(builddir) --format=wheel


$(sdist) : $(dist_files)
	$(POETRY) --output $(builddir) --format=sdist


# PHONY TARGETS #
#################

# Build all binary targets necessary for installation.
# Does not build documentation or source distributions.
all : $(wheels)
.PHONY : all


# Run pre-installation tests on the built artifacts.
check : all
	PYTHONPATH=. $(PYTEST) tests/unit/
.PHONY : check


# Remove all files created as a result of building the project.
clean : mostlyclean
	find ./ -depth -path '**/.pytest_cache*' -print -delete
	find ./ -depth -path '**/__pycache__*' -print -delete
	$(RUFF) clean
.PHONY : clean


# Build the redistributable source archive.
dist : $(sdist)
.PHONY : dist


# Check and publish the python package index artifacts.
publish : $(sdist) $(wheels)
	$(POETRY) publish --dist-dir=$(builddir)
.PHONY : publish


# Build the project's HTML documentation.
html :
	$(SPHINX_BUILD) --builder html docs $(builddir)/html
.PHONY : html


linkcheck :
	$(SPHINX_BUILD) --builder linkcheck docs $(builddir)/linkcheck
.PHONY : linkcheck


# Lint the project source for quality.
lint : linkcheck
	$(POETRY) check --strict
	$(RUFF) check $(srcdir)
.PHONY : lint


# Remove files created as a result of building the project, except those that
# rarely need to be rebuilt.
mostlyclean :
	rm -rf $(builddir)
	find ./ -depth -path '**/rule34Py.egg-info*' -print -delete
.PHONY : mostlyclean
