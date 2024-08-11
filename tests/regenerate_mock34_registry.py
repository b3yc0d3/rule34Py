#!/usr/bin/env python3
"""This script deletes and regenerates the whole of the mock34 responses registry.
"""

import os
import sys
import logging
from pathlib import Path

import pytest

logger = logging.getLogger(Path(__file__).name)
logging.basicConfig(level=logging.DEBUG)  # set to logging.DEBUG if there are issues

if len(sys.argv) < 2 or sys.argv[1].lower() != "-y":
	# Issue a user-warning, if this script was called without the special '-y' flag.
	# This helps to save users who accidentally call this script.
	sys.stderr.write("WARNING: This script will delete your Mock34 test fixture responses file. If you mean to do that, call this script with the '-y' flag.\n")
	sys.exit(2)

logger.info("Adding project root to PYTHONPATH.")
sys.path.insert(0, str(Path(__file__).parent.parent.resolve()))
logger.debug(f"sys.path={sys.path}")

from tests.fixtures.mock34 import REGISTRY_FILE

if REGISTRY_FILE.exists():
	logger.info(f"Removing responses.yml file at \"{REGISTRY_FILE}\".")
	os.remove(REGISTRY_FILE)
else:
	logger.debug("Registry file does not exist.")

logger.info("Regenerating registry file by running all tests.")
os.environ["R34_RECORD_RESPONSES"] = "True"
pytest.main(["."])

sys.exit(0)
