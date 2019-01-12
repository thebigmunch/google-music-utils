from google_music_utils import find_existing_items, find_missing_items
from google_music_utils.compare import _gather_field_values

from .fixtures import (
	TEST_FORMAT_1,
	TEST_MAPPING_1,
	TEST_MAPPING_2,
	TEST_MAPPING_ITEMS_1,
	TEST_MAPPING_ITEMS_2,
	TEST_MAPPING_ITEMS_3,
	TEST_PATH_1,
)


class TestGatherFieldValues:
	def test_inputs(self):
		_gather_field_values(TEST_FORMAT_1)
		_gather_field_values(TEST_MAPPING_1)
		_gather_field_values(TEST_PATH_1)


class TestExistingItems:
	def test_no_fields_same(self):
		existing = list(
			find_existing_items(
				TEST_MAPPING_ITEMS_1,
				TEST_MAPPING_ITEMS_1
			)
		)
		expected = TEST_MAPPING_ITEMS_1

		assert existing == expected

	def test_no_fields_different(self):
		existing = list(
			find_existing_items(
				TEST_MAPPING_ITEMS_2,
				TEST_MAPPING_ITEMS_3
			)
		)
		expected = []

		assert existing == expected

	def test_no_fields_partial(self):
		existing = list(
			find_existing_items(
				TEST_MAPPING_ITEMS_1,
				TEST_MAPPING_ITEMS_2
			)
		)
		expected = [TEST_MAPPING_1]

		assert existing == expected

	def test_fields_same(self):
		existing = list(
			find_existing_items(
				TEST_MAPPING_ITEMS_1,
				TEST_MAPPING_ITEMS_1,
				fields=['artist', 'album']
			)
		)
		expected = TEST_MAPPING_ITEMS_1

		assert existing == expected

	def test_fields_different(self):
		existing = list(
			find_existing_items(
				TEST_MAPPING_ITEMS_2,
				TEST_MAPPING_ITEMS_3,
				fields=['artist', 'album']
			)
		)
		expected = []

		assert existing == expected

	def test_fields_partial(self):
		existing = list(
			find_existing_items(
				TEST_MAPPING_ITEMS_1,
				TEST_MAPPING_ITEMS_2,
				fields=['artist', 'title']
			)
		)
		expected = [TEST_MAPPING_1]

		assert existing == expected

	def test_default_field_map(self):
		existing = list(
			find_existing_items(
				TEST_MAPPING_ITEMS_1,
				TEST_MAPPING_ITEMS_2,
				fields=['tracknumber']
			)
		)
		expected = [TEST_MAPPING_1]

		assert existing == expected

	def test_default_field_map_no_exist(self):
		existing = list(
			find_existing_items(
				TEST_MAPPING_ITEMS_1,
				TEST_MAPPING_ITEMS_2,
				fields=['tracknumber', 'noexist']
			)
		)
		expected = [TEST_MAPPING_1]

		assert existing == expected

	def test_custom_field_map(self):
		existing = list(
			find_existing_items(
				TEST_MAPPING_ITEMS_1,
				TEST_MAPPING_ITEMS_2,
				fields=['tracknumber'],
				field_map={'tracknumber': 'track_number'}
			)
		)
		expected = [TEST_MAPPING_1]

		assert existing == expected

	def test_custom_field_map_no_exist(self):
		existing = list(
			find_existing_items(
				TEST_MAPPING_ITEMS_1,
				TEST_MAPPING_ITEMS_2,
				fields=['tracknumber'],
				field_map={'tracknumber': 'track_number', 'noexist': 'no_exist'}
			)
		)
		expected = [TEST_MAPPING_1]

		assert existing == expected


class TestMissingItems:
	def test_no_fields_same(self):
		missing = list(
			find_missing_items(
				TEST_MAPPING_ITEMS_1,
				TEST_MAPPING_ITEMS_1
			)
		)
		expected = []

		assert missing == expected

	def test_no_fields_different(self):
		missing = list(
			find_missing_items(
				TEST_MAPPING_ITEMS_2,
				TEST_MAPPING_ITEMS_3
			)
		)
		expected = TEST_MAPPING_ITEMS_2

		assert missing == expected

	def test_no_fields_partial(self):
		missing = list(
			find_missing_items(
				TEST_MAPPING_ITEMS_1,
				TEST_MAPPING_ITEMS_2
			)
		)
		expected = [TEST_MAPPING_2]

		assert missing == expected

	def test_fields_same(self):
		missing = list(
			find_missing_items(
				TEST_MAPPING_ITEMS_1,
				TEST_MAPPING_ITEMS_1,
				fields=['artist', 'album']
			)
		)
		expected = []

		assert missing == expected

	def test_fields_different(self):
		missing = list(
			find_missing_items(
				TEST_MAPPING_ITEMS_2,
				TEST_MAPPING_ITEMS_3,
				fields=['artist', 'album']
			)
		)
		expected = TEST_MAPPING_ITEMS_2

		assert missing == expected

	def test_fields_partial(self):
		missing = list(
			find_missing_items(
				TEST_MAPPING_ITEMS_1,
				TEST_MAPPING_ITEMS_2,
				fields=['artist', 'title']
			)
		)
		expected = [TEST_MAPPING_2]

		assert missing == expected

	def test_default_field_map(self):
		missing = list(
			find_missing_items(
				TEST_MAPPING_ITEMS_1,
				TEST_MAPPING_ITEMS_2,
				fields=['tracknumber']
			)
		)
		expected = [TEST_MAPPING_2]

		assert missing == expected

	def test_default_field_map_no_exist(self):
		missing = list(
			find_missing_items(
				TEST_MAPPING_ITEMS_1,
				TEST_MAPPING_ITEMS_2,
				fields=['tracknumber', 'noexist']
			)
		)
		expected = [TEST_MAPPING_2]

		assert missing == expected

	def test_custom_field_map(self):
		missing = list(
			find_missing_items(
				TEST_MAPPING_ITEMS_1,
				TEST_MAPPING_ITEMS_2,
				fields=['tracknumber'],
				field_map={'tracknumber': 'track_number'}
			)
		)
		expected = [TEST_MAPPING_2]

		assert missing == expected

	def test_custom_field_map_no_exist(self):
		missing = list(
			find_missing_items(
				TEST_MAPPING_ITEMS_1,
				TEST_MAPPING_ITEMS_2,
				fields=['tracknumber'],
				field_map={'tracknumber': 'track_number', 'noexist': 'no_exist'}
			)
		)
		expected = [TEST_MAPPING_2]

		assert missing == expected
