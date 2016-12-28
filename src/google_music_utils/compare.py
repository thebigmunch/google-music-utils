__all__ = ['compare_item_collections']

import audio_metadata
from multidict import MultiDict

from .constants import FIELD_MAP
from .utils import list_to_single_value, normalize_value


def _gather_field_values(item, *, fields=None, field_map=FIELD_MAP, normalize_values=False):
	"""Create a tuple of normalized metadata field values.

	Parameter:
		item (dict): Item dict or filepath.
		fields (list): A sequence of fields used to compare item dicts.
		normalize_values (bool): Normalize metadata values to remove common differences between sources.
			Default: ``False``

	Returns:
		tuple: Values from the given metadata fields.
	"""

	if not isinstance(item, (audio_metadata.Format, dict)):
		item = audio_metadata.load(item).tags  # pragma: no cover

	if fields is None:
		if hasattr(item, 'FIELD_MAP'):
			fields = [item.FIELD_MAP.get(k, k) for k in item]
		else:
			fields = list(item.keys())

	normalize = normalize_value if normalize_values else lambda x: str(x)

	field_values = []

	for field in fields:
		if item.get(field):
			field_values.append(normalize(list_to_single_value(item[field])))
		elif isinstance(field_map, MultiDict):
			for alias in field_map.getall(field, []):
				if item.get(alias):  # pragma: no branch
					field_values.append(normalize(list_to_single_value(item[alias])))
					break
		elif isinstance(field_map, dict):  # pragma: no branch
			alias = field_map.get(field)

			if alias in item:  # pragma: no branch
				field_values.append(normalize(list_to_single_value(item[alias])))

	return tuple(field_values)


def compare_item_collections(src, dst, *, fields=None, field_map=None, normalize_values=False):
	"""Find items from an item collection that are not in another item collection.

	Parameters:
		src (list): A sequence of item dicts or filepaths.
		dst (list): A sequence of item dicts or filepaths.
		fields (list): A sequence of fields used to compare item dicts.
		normalize_values (bool): Normalize metadata values to remove common differences between sources.
			Default: ``False``

	Yields:
		dict: The next item from ``src`` collection not in ``dst`` collection.

	Example:
		>>> from google_music_utils import compare_item_collections
		>>> list(compare_item_collections(song_list_1, song_list_2, fields=['artist', 'album', 'title']))
	"""

	if field_map is None:
		field_map = FIELD_MAP

	dst_keys = {
		_gather_field_values(
			dst_item, fields=fields, field_map=field_map, normalize_values=normalize_values
		) for dst_item in dst
	}

	for src_item in src:
		if _gather_field_values(
			src_item, fields=fields, field_map=field_map, normalize_values=normalize_values
		) not in dst_keys:
			yield src_item
