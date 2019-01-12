__all__ = ['find_existing_items', 'find_missing_items']

import os
from collections.abc import Mapping

import audio_metadata
from multidict import MultiDict

from .constants import FIELD_MAP
from .utils import list_to_single_value, normalize_value


def _gather_field_values(
	item, *, fields=None, field_map=FIELD_MAP,
	normalize_values=False, normalize_func=normalize_value):
	"""Create a tuple of normalized metadata field values.

	Parameter:
		item (~collections.abc.Mapping, str, os.PathLike): Item dict or filepath.
		fields (list): A list of fields used to compare item dicts.
		field_map (~collections.abc.Mapping): A mapping field name aliases.
			Default: :data:`~google_music_utils.constants.FIELD_MAP`
		normalize_values (bool): Normalize metadata values to remove common differences between sources.
			Default: ``False``
		normalize_func (function): Function to apply to metadata values if
			``normalize_values`` is ``True``.
			Default: :func:`~google_music_utils.utils.normalize_value`

	Returns:
		tuple: Values from the given metadata fields.
	"""

	if isinstance(item, (str, os.PathLike)):
		it = audio_metadata.load(item).tags
	elif isinstance(item, audio_metadata.Format):
		it = item.tags
	else:
		it = item

	if fields is None:
		if hasattr(it, 'FIELD_MAP'):
			fields = [it.FIELD_MAP.get(k, k) for k in it]
		else:
			fields = list(it.keys())

	normalize = normalize_func if normalize_values else lambda x: str(x)

	field_values = []

	for field in fields:
		if it.get(field):
			field_values.append(normalize(list_to_single_value(it[field])))
		elif isinstance(field_map, MultiDict):
			for alias in field_map.getall(field, []):
				if it.get(alias):  # pragma: no branch
					field_values.append(normalize(list_to_single_value(it[alias])))
					break
		elif isinstance(field_map, Mapping):  # pragma: no branch
			alias = field_map.get(field)

			if alias in it:  # pragma: no branch
				field_values.append(normalize(list_to_single_value(it[alias])))

	return tuple(field_values)


def find_existing_items(
	src, dst, *, fields=None, field_map=None,
	normalize_values=False, normalize_func=normalize_value):
	"""Find items from an item collection that are in another item collection.

	Parameters:
		src (list): A list of item dicts or filepaths.
		dst (list): A list of item dicts or filepaths.
		fields (list): A list of fields used to compare item dicts.
		field_map (~collections.abc.Mapping): A mapping field name aliases.
			Default: :data:`~google_music_utils.constants.FIELD_MAP`
		normalize_values (bool): Normalize metadata values to remove common differences between sources.
			Default: ``False``
		normalize_func (function): Function to apply to metadata values if
			``normalize_values`` is ``True``.
			Default: :func:`~google_music_utils.utils.normalize_value`

	Yields:
		dict: The next item from ``src`` collection in ``dst`` collection.
	"""

	if field_map is None:
		field_map = FIELD_MAP

	dst_keys = {
		_gather_field_values(
			dst_item, fields=fields, field_map=field_map,
			normalize_values=normalize_values, normalize_func=normalize_func
		) for dst_item in dst
	}

	for src_item in src:
		if _gather_field_values(
			src_item, fields=fields, field_map=field_map,
			normalize_values=normalize_values, normalize_func=normalize_func
		) in dst_keys:
			yield src_item


def find_missing_items(
	src, dst, *, fields=None, field_map=None,
	normalize_values=False, normalize_func=normalize_value):
	"""Find items from an item collection that are not in another item collection.

	Parameters:
		src (list): A list of item dicts or filepaths.
		dst (list): A list of item dicts or filepaths.
		fields (list): A list of fields used to compare item dicts.
		field_map (~collections.abc.Mapping): A mapping field name aliases.
			Default: :data:`~google_music_utils.constants.FIELD_MAP`
		normalize_values (bool): Normalize metadata values to remove common differences between sources.
			Default: ``False``
		normalize_func (function): Function to apply to metadata values if
			``normalize_values`` is ``True``.
			Default: :func:`~google_music_utils.utils.normalize_value`

	Yields:
		dict: The next item from ``src`` collection not in ``dst`` collection.
	"""

	if field_map is None:
		field_map = FIELD_MAP

	dst_keys = {
		_gather_field_values(
			dst_item, fields=fields, field_map=field_map,
			normalize_values=normalize_values, normalize_func=normalize_func
		) for dst_item in dst
	}

	for src_item in src:
		if _gather_field_values(
			src_item, fields=fields, field_map=field_map,
			normalize_values=normalize_values, normalize_func=normalize_func
		) not in dst_keys:
			yield src_item
