# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from datetime import datetime
from pathlib import Path
import sys

if sys.version_info < (3, 11):
    import tomli as toml
else:
    import tomllib as toml

PROJECT_ROOT = Path(__file__).parent.resolve() / ".."

# Read the pyproject.toml
with open(PROJECT_ROOT / "pyproject.toml", "rb") as fp_pyproject:
    pyproject = toml.load(fp_pyproject)
authors = [m["name"] for m in pyproject["project"]["authors"]]

project = pyproject["project"]["name"]
copyright = str(datetime.now().year) + ', b3yc0d3'
author = ", ".join(authors)
release = pyproject["project"]["version"]


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_mdinclude",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.duration",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
]

templates_path = ['_templates']
exclude_patterns = []

# sphinx.ext.autodoc configuration #
autodoc_default_options = {
    "private-members": False
}
autodoc_typehints = "both"  # Show typehints in the signature and as content of the function or method

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "requests": ("https://requests.readthedocs.io/en/latest/", None),
}

## Sphinx linkcheck options
linkcheck_ignore = [
    r"https?://.*gnu.org(:\d+)?[/$]?.*",  # GNU.org is heavily rate limited
    r"https?://localhost(:\d+)?[/$]?.*",  # Broken unless the dev is hosting a server.
    r"https?://rule34.xxx(:\d+)?[/$]?.*",  # Interactive site will always 403
]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
