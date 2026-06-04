# rule34Py - Python api wrapper for rule34.xxx
#
# Copyright (C) 2026 b3yc0d3 <b3yc0d3@gmail.com>
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

"""A module containing the Tag class."""

from enum import Enum

class TagType(Enum):
	"""
	Possible type of a tag
	"""

	ARTIST = 1
	"""
	Artist name
	"""
	CHARACTER = 2
	"""
	Character name
	"""
	COPYRIGHT = 3
	"""
	Copyright holder
	"""
	METADATA = 4
	"""
	Metadata generic
	"""
	TAG = 0
	"""
	Tag generic
	"""

	@staticmethod
	def from_str(data: str):
		"""Convert str into TagType.

		Args:
			data (str): Lowercase representation of tag type.

		Returns:
			Type of Tag
		"""

		data = data.lower()

		if data == "artist":
			return TagType.ARTIST
		elif data == "character":
			return TagType.CHARACTER
		elif data == "copyright":
			return TagType.COPYRIGHT
		else:
			return TagType.TAG

# TODO: implement also STR methods for this class
class Tag:
	"""A Rule34 Tag object.

	Note:
		This object can behave as a normal string, for backwards compatibility.

	Parameters:
		count: Usage count of the Tag.
		type: Type of the Tag.
		tag: String value of the Tag.
	"""

	count: int
	type: TagType
	tag: str

	@staticmethod
	def from_json(json: dict) -> Tag:
		"""Create Tag class instance from JSON data.

		Args:
			json (dict): Tag json object.
		"""

		_count = int(json["count"])
		_type = TagType.from_str(json["type"])
		_tag = json["tag"]

		return Tag(_count, _type, _tag)

	def __init__(self, count: int, type: TagType, tag: str):
		"""
		Create a new Tag object.
		"""

		self._count = count
		self._type = type
		self._tag = tag

	@property
	def count(self) -> int:
		"""Usage count of the Tag.

		Returns:
			The count how often the Tag is used.
		"""
		return self._count

	@property
	def type(self) -> TagType:
		"""Type of the Tag

		Returns:
			The type of the current tag
		"""
		return self._type

	@property
	def tag(self) -> str:
		"""Value of the Tag.

		Returns:
			The string value of the tag.
		"""
		return self._tag

	def __str__(self) -> str:
		return self.tag

	def __getattr__(self, name: str):
		"""
		Is here for backwards compatibility
		"""
		return getattr(self.tag, name)