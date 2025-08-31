# rule34Py - Python api wrapper for rule34.xxx
# 
# Copyright (C) 2022-2025 b3yc0d3 <b3yc0d3@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""Provides the AutocompleteTag class used for tag suggestions from Rule34 autocomplete."""

from dataclasses import dataclass
from typing import Union

@dataclass
class AutocompleteTag:
    """Represents a tag suggestion from autocomplete.

        .. important::
            
            Do to switching from the website endpoint to the REST API endpoint, the``type`` is currently always **None**.

    Parameters:
        label: The full tag label including count (e.g., "hooves (95430)").
        value: The clean tag value (e.g., "hooves").
        type: The tag category (e.g., "general", "copyright").
    """

    #: The full tag label including count (e.g., "hooves (95430)").
    label: str
    #: The clean tag value without count information.
    value: str
    #: The category of the tag (general/copyright/other).
    #:
    #: .. important::
    #:
    #:     Do to switching from the website endpoint to the REST API endpoint, the``type`` is currently always **None**.
    type: Union[str, None]