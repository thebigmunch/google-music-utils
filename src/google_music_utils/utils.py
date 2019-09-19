__all__ = [
	'get_field',
	'list_to_single_value',
	'normalize_value',
]

import os
import re
from collections.abc import Mapping

import audio_metadata
from audio_metadata import AudioMetadataException
from multidict import MultiDict

from .constants import FIELD_MAP


def get_field(tags, field, default='', *, field_map=FIELD_MAP):
	value = default
	try:
		value = tags[field]
	except KeyError:
		if isinstance(field_map, MultiDict):
			for alias in field_map.getall(field, []):
				if tags.get(alias):  # pragma: no branch
					value = tags[alias]
					break
		elif isinstance(field_map, Mapping):  # pragma: no branch
			alias = field_map.get(field)

			if alias in tags:  # pragma: no branch
				value = tags[alias]

	return value


def get_item_tags(item):
	if isinstance(item, (str, os.PathLike)):
		try:
			tags = audio_metadata.load(item).tags
		except AudioMetadataException:
			tags = None
	elif isinstance(item, audio_metadata.Format):
		tags = item.tags
	else:
		tags = item

	return tags


def list_to_single_value(value):
	if not isinstance(value, (list, tuple)):
		return value

	return value[0]


def normalize_value(value):
	"""Normalize metadata value to improve match accuracy."""

	value = str(value)
	value = value.casefold()

	value = re.sub(r'\/\s*\d+', '', value)  # Remove "/<totaltracks>" from track number.
	value = re.sub(
		r'^0+([0-9]+)', r'\1', value
	)  # Remove leading zero(s) from track number.
	value = re.sub(r'^(\d+)\.+', r'\1', value)  # Remove dots from track number.
	value = re.sub(r'[^\w\s]', '', value)  # Remove leading non-word characters.
	value = re.sub(r'^the\s+', '', value)  # Remove leading "the".
	value = re.sub(r'^\s+', '', value)  # Remove leading spaces.
	value = re.sub(r'\s+$', '', value)  # Remove trailing spaces.
	value = re.sub(r'\s+', ' ', value)  # Reduce multiple spaces to a single space.

	return value
