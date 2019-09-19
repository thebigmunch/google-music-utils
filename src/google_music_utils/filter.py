__all__ = [
	'exclude_items',
	'include_items',
]

import functools
import re
from itertools import filterfalse


from .utils import (
	get_field,
	get_item_tags,
	normalize_value,
)


def _match_field(
	field_value,
	pattern,
	*,
	ignore_case=False,
	normalize_values=False
):
	"""Match an item metadata field value by pattern.

	Note:
		Metadata values are lowercased when ``normalized_values`` is ``True``,
		so ``ignore_case`` is automatically set to ``True``.

	Parameters:
		field_value (list or str): A metadata field value to check.
		pattern (str): A regex pattern to check the field value(s) against.
		ignore_case (bool, Optional):
			Perform case-insensitive matching.
			Default: ``False``
		normalize_values (bool, Optional):
			Normalize metadata values to remove common differences between sources.
			Default: ``False``

	Returns:
		bool: True if matched, False if not.
	"""

	if normalize_values:
		ignore_case = True

	normalize = normalize_value if normalize_values else lambda x: str(x)
	search = functools.partial(re.search, flags=re.I) if ignore_case else re.search

	# audio_metadata fields contain a list of values.
	if isinstance(field_value, list):
		return any(search(pattern, normalize(value)) for value in field_value)
	else:
		return search(pattern, normalize(field_value))


def _match_item(
	item,
	*,
	any_all=any,
	ignore_case=False,
	normalize_values=False,
	**kwargs
):
	"""Match items by metadata.

	Note:
		Metadata values are lowercased when ``normalized_values`` is ``True``,
		so ``ignore_case`` is automatically set to ``True``.

	Parameters:
		item (~collections.abc.Mapping, str, os.PathLike): Item dict or filepath.
		any_all (callable, Optional):
			A callable to determine if any or all filters must match to match item.
			Expected values :obj:`any` (default) or :obj:`all`.
		ignore_case (bool, Optional):
			Perform case-insensitive matching.
			Default: ``False``
		normalize_values (bool, Optional):
			Normalize metadata values to remove common differences between sources.
			Default: ``False``
		kwargs (list, Optional): Lists of values to match the given metadata field.

	Returns:
		bool: True if matched, False if not.
	"""

	tags = get_item_tags(item)

	if tags is not None:
		return any_all(
			_match_field(
				get_field(tags, field),
				pattern,
				ignore_case=ignore_case,
				normalize_values=normalize_values,
			)
			for field, patterns in kwargs.items()
			for pattern in patterns
		)


def exclude_items(
	items,
	*,
	any_all=any,
	ignore_case=False,
	normalize_values=False,
	**kwargs
):
	"""Exclude items by matching metadata.

	Note:
		Metadata values are lowercased when ``normalized_values`` is ``True``,
		so ``ignore_case`` is automatically set to ``True``.

	Parameters:
		items (list): A list of item dicts or filepaths.
		any_all (callable, Optional):
			A callable to determine if any or all filters must match to exclude items.
			Expected values :obj:`any` (default) or :obj:`all`.
		ignore_case (bool, Optional):
			Perform case-insensitive matching.
			Default: ``False``
		normalize_values (bool, Optional):
			Normalize metadata values to remove common differences between sources.
			Default: ``False``
		kwargs (list, Optional): Lists of values to match the given metadata field.

	Yields:
		dict: The next item to be included.

	Example:
		>>> from google_music_utils import exclude_items
		>>> list(exclude_items(song_list, any_all=all, ignore_case=True, normalize_values=True, artist=['Beck'], album=['Golden Feelings']))
	"""

	if kwargs:
		match = functools.partial(
			_match_item,
			any_all=any_all,
			ignore_case=ignore_case,
			normalize_values=normalize_values,
			**kwargs
		)

		return filterfalse(match, items)
	else:
		return iter(items)


def include_items(
	items,
	*,
	any_all=any,
	ignore_case=False,
	normalize_values=False,
	**kwargs
):
	"""Include items by matching metadata.

	Note:
		Metadata values are lowercased when ``normalized_values`` is ``True``,
		so ``ignore_case`` is automatically set to ``True``.

	Parameters:
		items (list): A list of item dicts or filepaths.
		any_all (callable, Optional):
			A callable to determine if any or all filters must match to include items.
			Expected values :obj:`any` (default) or :obj:`all`.
		ignore_case (bool, Optional):
			Perform case-insensitive matching.
			Default: ``False``
		normalize_values (bool, Optional):
			Normalize metadata values to remove common differences between sources.
			Default: ``False``
		kwargs (list, Optional): Lists of values to match the given metadata field.

	Yields:
		dict: The next item to be included.

	Example:
		>>> from google_music_utils import exclude_items
		>>> list(include_items(song_list, any_all=all, ignore_case=True, normalize_values=True, artist=['Beck'], album=['Odelay']))
	"""

	if kwargs:
		match = functools.partial(
			_match_item,
			any_all=any_all,
			ignore_case=ignore_case,
			normalize_values=normalize_values,
			**kwargs
		)

		return filter(match, items)
	else:
		return iter(items)
