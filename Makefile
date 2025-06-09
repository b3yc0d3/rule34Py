# Extract the project name and version from the pyproject.toml file.
PROJECT = $(shell $(PYTHON3) scripts/read_pyproject.py project/name | tr 'A-Z' 'a-z')
VERSION = $(shell $(PYTHON3) scripts/read_pyproject.py project/version)

# Binaries
PYTHON3 ?= python3
PYTEST = $(PYTHON3) -m pytest
PYTHON_BUILD = $(PYTHON3) -m build
RUFF = $(PYTHON3) -m ruff
SPHINX = $(PYTHON3) -m sphinx
TWINE = $(PYTHON3) -m twine

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
	$(PYTHON_BUILD) --outdir $(builddir) --wheel


$(sdist) : $(dist_files)
	$(PYTHON_BUILD) --outdir $(builddir) --sdist


# PHONY TARGETS #
#################

# Build all binary targets necessary for installation.
# Does not build documentation or source distributions.
all : $(wheels)
.PHONY : all


# Run pre-installation tests on the built artifacts.
check : all
	PYTHONPATH=$(builddir)/lib $(PYTEST) tests/unit/
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
	$(TWINE) check $(^)
	$(TWINE) upload $(^)
.PHONY : publish


# Build the project's HTML documentation.
html :
	$(SPHINX) --builder html docs $(builddir)/html
.PHONY : html


# Lint the project source for quality.
lint :
	$(RUFF) check $(srcdir)
.PHONY : lint


# Remove files created as a result of building the project, except those that
# rarely need to be rebuilt.
mostlyclean :
	rm -rf $(builddir)
	find ./ -depth -path '**/rule34Py.egg-info*' -print -delete
.PHONY : mostlyclean
