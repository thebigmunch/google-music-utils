__all__ = ['list_to_single_value', 'normalize_value']

import re


def list_to_single_value(value):
	if not isinstance(value, (list, tuple)):
		return value

	return value[0]


def normalize_value(value):
	"""Normalize metadata value to improve match accuracy."""

	value = str(value)
	value = value.lower()

	value = re.sub(r'\/\s*\d+', '', value)  # Remove "/<totaltracks>" from track number.
	value = re.sub(r'^0+([0-9]+)', r'\1', value)  # Remove leading zero(s) from track number.
	value = re.sub(r'^(\d+)\.+', r'\1', value)  # Remove dots from track number.
	value = re.sub(r'[^\w\s]', '', value)  # Remove leading non-word characters.
	value = re.sub(r'^the\s+', '', value)  # Remove leading "the".
	value = re.sub(r'^\s+', '', value)  # Remove leading spaces.
	value = re.sub(r'\s+$', '', value)  # Remove trailing spaces.
	value = re.sub(r'\s+', ' ', value)  # Reduce multiple spaces to a single space.

	return value
