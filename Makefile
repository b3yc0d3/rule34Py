
.DEFAULT_GOAL = all

PROJECT = rule34py
VERSION = $(shell git describe --tags)

TWINE = twine upload dist/*
PYTHON3 ?= python3
PYTHON_BUILD = $(PYTHON3) -m build
RUFF = $(PYTHON3) -m ruff
SPHINX_BUILD = $(PYTHON3) -m sphinx
PYTEST = $(PYTHON3) -m pytest

builddir ?= build
srcdir = rule34Py

# Installation Directories
prefix ?= /usr/local

docdir ?= $(prefix)/share/doc/$(project)
htmldir ?= $(docdir)/html


# REAL TARGETS #
################


# PHONY TARGETS #
#################

all : html
	$(PYTHON3) -m build --wheel --outdir $(builddir) --verbose
.PHONY : all


check :
	PYTHONPATH=$(srcdir)/.. $(PYTEST) tests/unit/
.PHONY : check


clean : mostlyclean
	find ./ -depth -path '**/.pytest_cache*' -print -delete
	find ./ -depth -path '**/__pycache__*' -print -delete
	$(RUFF) clean
.PHONY : clean


dist :
	$(PYTHON_BUILD) --sdist --outdir $(builddir)
.PHONY : dist

publish : clean dist
	$(TWINE)
.PHONY : publish


distclean : clean
.PHONY : distclean


html :
	$(SPHINX_BUILD) --builder html docs $(builddir)/html
.PHONY : html


lint :
	$(RUFF) check $(srcdir)
.PHONY : lint


mostlyclean :
	rm -rf $(builddir)
	find ./ -depth -path '**/rule34Py.egg-info*' -print -delete
.PHONY : mostlyclean
