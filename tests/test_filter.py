from google_music_utils import exclude_items, include_items

from .fixtures import TEST_COLLECTION_1


class TestIncludeItems:
	def test_include_items_no_filters(self):
		included_any = list(include_items(TEST_COLLECTION_1, any_all=any))
		included_all = list(include_items(TEST_COLLECTION_1, any_all=all))
		expected = TEST_COLLECTION_1

		assert included_any == included_all == expected

	def test_include_items_single_match(self):
		included_any = list(include_items(TEST_COLLECTION_1, any_all=any, title=['Take']))
		included_all = list(include_items(TEST_COLLECTION_1, any_all=all, title=['Take']))
		expected = [TEST_COLLECTION_1[0]]

		assert included_any == included_all == expected

	def test_include_items_single_no_match(self):
		included_any = list(include_items(TEST_COLLECTION_1, any_all=any, artist=['Modest']))
		included_all = list(include_items(TEST_COLLECTION_1, any_all=any, artist=['Modest']))
		expected = []

		assert included_any == included_all == expected

	def test_include_items_any_multiple_match(self):
		included = list(include_items(TEST_COLLECTION_1, any_all=any, artist=['Muse'], title=['Take']))
		expected = TEST_COLLECTION_1

		assert included == expected

	def test_include_items_any_mutliple_no_match(self):
		included = list(include_items(TEST_COLLECTION_1, any_all=any, artist=['Modest'], title=['Everything']))
		expected = []

		assert included == expected

	def test_include_items_all_multiple_match(self):
		included = list(include_items(TEST_COLLECTION_1, any_all=all, artist=['Muse'], title=['Take']))
		expected = [TEST_COLLECTION_1[0]]

		assert included == expected

	def test_include_items_all_mutliple_no_match(self):
		included = list(include_items(TEST_COLLECTION_1, any_all=all, artist=['Modest'], title=['Everything']))
		expected = []

		assert included == expected


class TestExcludeItems:
	def test_exclude_items_no_filters(self):
		included_any = list(exclude_items(TEST_COLLECTION_1, any_all=any))
		included_all = list(exclude_items(TEST_COLLECTION_1, any_all=all))
		expected = TEST_COLLECTION_1

		assert included_any == included_all == expected

	def test_exclude_items_single_match(self):
		included_any = list(exclude_items(TEST_COLLECTION_1, any_all=any, title=['Take']))
		included_all = list(exclude_items(TEST_COLLECTION_1, any_all=all, title=['Take']))
		expected = [TEST_COLLECTION_1[1]]

		assert included_any == included_all == expected

	def test_exclude_items_single_no_match(self):
		included_any = list(exclude_items(TEST_COLLECTION_1, any_all=any, artist=['Modest']))
		included_all = list(exclude_items(TEST_COLLECTION_1, any_all=any, artist=['Modest']))
		expected = TEST_COLLECTION_1

		assert included_any == included_all == expected

	def test_exclude_items_any_multiple_match(self):
		included = list(exclude_items(TEST_COLLECTION_1, any_all=any, artist=['Muse'], title=['Take']))
		expected = []

		assert included == expected

	def test_exclude_items_any_mutliple_no_match(self):
		included = list(exclude_items(TEST_COLLECTION_1, any_all=any, artist=['Modest'], title=['Everything']))
		expected = TEST_COLLECTION_1

		assert included == expected

	def test_exclude_items_all_multiple_match(self):
		included = list(exclude_items(TEST_COLLECTION_1, any_all=all, artist=['Muse'], title=['Take']))
		expected = [TEST_COLLECTION_1[1]]

		assert included == expected

	def test_exclude_items_all_mutliple_no_match(self):
		included = list(exclude_items(TEST_COLLECTION_1, any_all=all, artist=['Modest'], title=['Everything']))
		expected = TEST_COLLECTION_1

		assert included == expected
