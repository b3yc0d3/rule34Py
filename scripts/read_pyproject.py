#!/usr/bin/env python3
"""Generate a Makefile includes file which exports variables from the pyproject.toml."""

from pathlib import Path
import sys

if sys.version_info < (3, 11):
    import tomli as toml
else:
    import tomllib as toml

PROJECT_ROOT = Path(__file__).parents[1].resolve()

with open(PROJECT_ROOT / "pyproject.toml", "rb") as fp_pyproject:
    pyproject_data = toml.load(fp_pyproject)


for path in sys.argv[1:]:
    path_elements = path.split("/")

    cursor = pyproject_data
    for path_element in path_elements:
        cursor = cursor[path_element]
    sys.stdout.write(str(cursor) + "\n")
