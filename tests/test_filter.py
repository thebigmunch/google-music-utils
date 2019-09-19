import pytest
from google_music_utils import (
	exclude_items,
	include_items
)
from google_music_utils.filter import _match_item

from .fixtures import (
	TEST_FORMAT_1,
	TEST_MAPPING_1,
	TEST_MAPPING_ITEMS_1,
	TEST_PATH_1,
)


class TestMatchItem:
	@pytest.mark.parametrize(
		'item',
		[
			TEST_FORMAT_1,
			TEST_MAPPING_1,
			TEST_PATH_1
		]
	)
	def test_inputs(self, item):
		matched = _match_item(item, artist=["Muse"])

		assert matched is True

	def test_ignore_case(self):
		matched = _match_item(TEST_MAPPING_1, artist=["Muse"])
		not_matched = _match_item(TEST_MAPPING_1, artist=["muse"])

		assert matched is True
		assert not_matched is False

	def test_ignore_case_switch(self):
		matched = _match_item(TEST_MAPPING_1, normalize_values=True, artist=["muse"])

		assert matched is True

	def test_unsupported_format(self):
		matched = _match_item(__file__)

		assert matched is None


class TestIncludeItems:
	def test_include_items_no_filters(self):
		included_any = list(include_items(TEST_MAPPING_ITEMS_1, any_all=any))
		included_all = list(include_items(TEST_MAPPING_ITEMS_1, any_all=all))
		expected = TEST_MAPPING_ITEMS_1

		assert included_any == included_all == expected

	def test_include_items_single_match(self):
		included_any = list(include_items(TEST_MAPPING_ITEMS_1, any_all=any, title=['Take']))
		included_all = list(include_items(TEST_MAPPING_ITEMS_1, any_all=all, title=['Take']))
		expected = [TEST_MAPPING_ITEMS_1[0]]

		assert included_any == included_all == expected

	def test_include_items_single_no_match(self):
		included_any = list(include_items(TEST_MAPPING_ITEMS_1, any_all=any, artist=['Modest']))
		included_all = list(include_items(TEST_MAPPING_ITEMS_1, any_all=any, artist=['Modest']))
		expected = []

		assert included_any == included_all == expected

	def test_include_items_any_multiple_match(self):
		included = list(include_items(TEST_MAPPING_ITEMS_1, any_all=any, artist=['Muse'], title=['Take']))
		expected = TEST_MAPPING_ITEMS_1

		assert included == expected

	def test_include_items_any_mutliple_no_match(self):
		included = list(include_items(TEST_MAPPING_ITEMS_1, any_all=any, artist=['Modest'], title=['Everything']))
		expected = []

		assert included == expected

	def test_include_items_all_multiple_match(self):
		included = list(include_items(TEST_MAPPING_ITEMS_1, any_all=all, artist=['Muse'], title=['Take']))
		expected = [TEST_MAPPING_ITEMS_1[0]]

		assert included == expected

	def test_include_items_all_mutliple_no_match(self):
		included = list(include_items(TEST_MAPPING_ITEMS_1, any_all=all, artist=['Modest'], title=['Everything']))
		expected = []

		assert included == expected


class TestExcludeItems:
	def test_exclude_items_no_filters(self):
		included_any = list(exclude_items(TEST_MAPPING_ITEMS_1, any_all=any))
		included_all = list(exclude_items(TEST_MAPPING_ITEMS_1, any_all=all))
		expected = TEST_MAPPING_ITEMS_1

		assert included_any == included_all == expected

	def test_exclude_items_single_match(self):
		included_any = list(exclude_items(TEST_MAPPING_ITEMS_1, any_all=any, title=['Take']))
		included_all = list(exclude_items(TEST_MAPPING_ITEMS_1, any_all=all, title=['Take']))
		expected = [TEST_MAPPING_ITEMS_1[1]]

		assert included_any == included_all == expected

	def test_exclude_items_single_no_match(self):
		included_any = list(exclude_items(TEST_MAPPING_ITEMS_1, any_all=any, artist=['Modest']))
		included_all = list(exclude_items(TEST_MAPPING_ITEMS_1, any_all=any, artist=['Modest']))
		expected = TEST_MAPPING_ITEMS_1

		assert included_any == included_all == expected

	def test_exclude_items_any_multiple_match(self):
		included = list(exclude_items(TEST_MAPPING_ITEMS_1, any_all=any, artist=['Muse'], title=['Take']))
		expected = []

		assert included == expected

	def test_exclude_items_any_mutliple_no_match(self):
		included = list(exclude_items(TEST_MAPPING_ITEMS_1, any_all=any, artist=['Modest'], title=['Everything']))
		expected = TEST_MAPPING_ITEMS_1

		assert included == expected

	def test_exclude_items_all_multiple_match(self):
		included = list(exclude_items(TEST_MAPPING_ITEMS_1, any_all=all, artist=['Muse'], title=['Take']))
		expected = [TEST_MAPPING_ITEMS_1[1]]

		assert included == expected

	def test_exclude_items_all_mutliple_no_match(self):
		included = list(exclude_items(TEST_MAPPING_ITEMS_1, any_all=all, artist=['Modest'], title=['Everything']))
		expected = TEST_MAPPING_ITEMS_1

		assert included == expected
