__all__ = [
	'find_existing_items',
	'find_missing_items',
]

from .constants import FIELD_MAP
from .utils import (
	get_field,
	get_item_tags,
	list_to_single_value,
	normalize_value,
)


def _gather_field_values(
	item,
	*,
	fields=None,
	field_map=FIELD_MAP,
	normalize_values=False,
	normalize_func=normalize_value
):
	"""Create a tuple of normalized metadata field values.

	Parameter:
		item (~collections.abc.Mapping, str, os.PathLike): Item dict or filepath.
		fields (list, Optional): A list of fields used to compare item dicts.
		field_map (~collections.abc.Mapping, Optional):
			A mapping field name aliases.
			Default: :data:`~google_music_utils.constants.FIELD_MAP`
		normalize_values (bool, Optional):
			Normalize metadata values to remove common differences between sources.
			Default: ``False``
		normalize_func (callable, Optional):
			Function to apply to metadata values if ``normalize_values`` is ``True``.
			Default: :func:`~google_music_utils.utils.normalize_value`

	Returns:
		tuple: Values from the given metadata fields.
	"""

	tags = get_item_tags(item)

	if tags is not None:
		if fields is None:
			fields = list(tags.keys())

		normalize = normalize_func if normalize_values else lambda x: str(x)

		field_values = []

		for field in fields:
			field_values.append(
				normalize(
					list_to_single_value(
						get_field(tags, field, field_map=field_map)
					)
				)
			)

		return tuple(field_values)


def find_existing_items(
	src,
	dst,
	*,
	fields=None,
	field_map=None,
	normalize_values=False,
	normalize_func=normalize_value
):
	"""Find items from an item collection that are in another item collection.

	Parameters:
		src (list): A list of item dicts or filepaths.
		dst (list): A list of item dicts or filepaths.
		fields (list, Optional): A list of fields used to compare item dicts.
		field_map (~collections.abc.Mapping, Optional):
			A mapping field name aliases.
			Default: :data:`~google_music_utils.constants.FIELD_MAP`
		normalize_values (bool, Optional):
			Normalize metadata values to remove common differences between sources.
			Default: ``False``
		normalize_func (callable, Optional):
			Function to apply to metadata values if ``normalize_values`` is ``True``.
			Default: :func:`~google_music_utils.utils.normalize_value`

	Yields:
		dict: The next item from ``src`` collection in ``dst`` collection.
	"""

	if field_map is None:
		field_map = FIELD_MAP

	dst_keys = set()
	for dst_item in dst:
		field_values = _gather_field_values(
			dst_item,
			fields=fields,
			field_map=field_map,
			normalize_values=normalize_values,
			normalize_func=normalize_func,
		)

		if field_values is not None:
			dst_keys.add(field_values)

	for src_item in src:
		field_values = _gather_field_values(
			src_item,
			fields=fields,
			field_map=field_map,
			normalize_values=normalize_values,
			normalize_func=normalize_func,
		)

		if (
			field_values is not None
			and field_values in dst_keys
		):
			yield src_item


def find_missing_items(
	src,
	dst,
	*,
	fields=None,
	field_map=None,
	normalize_values=False,
	normalize_func=normalize_value
):
	"""Find items from an item collection that are not in another item collection.

	Parameters:
		src (list): A list of item dicts or filepaths.
		dst (list): A list of item dicts or filepaths.
		fields (list, Optional): A list of fields used to compare item dicts.
		field_map (~collections.abc.Mapping, Optional):
			A mapping field name aliases.
			Default: :data:`~google_music_utils.constants.FIELD_MAP`
		normalize_values (bool, Optional):
			Normalize metadata values to remove common differences between sources.
			Default: ``False``
		normalize_func (callable, Optional):
			Function to apply to metadata values if ``normalize_values`` is ``True``.
			Default: :func:`~google_music_utils.utils.normalize_value`

	Yields:
		dict: The next item from ``src`` collection not in ``dst`` collection.
	"""

	if field_map is None:
		field_map = FIELD_MAP

	dst_keys = set()
	for dst_item in dst:
		field_values = _gather_field_values(
			dst_item,
			fields=fields,
			field_map=field_map,
			normalize_values=normalize_values,
			normalize_func=normalize_func,
		)

		if field_values is not None:
			dst_keys.add(field_values)

	for src_item in src:
		field_values = _gather_field_values(
			src_item,
			fields=fields,
			field_map=field_map,
			normalize_values=normalize_values,
			normalize_func=normalize_func,
		)
		if (
			field_values is not None
			and field_values not in dst_keys
		):
			yield src_item
