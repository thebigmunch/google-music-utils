# TODO: Add metadata normalization tests.
# TODO: Add find_existing_items tests.

from google_music_utils import find_existing_items, find_missing_items

from .fixtures import TEST_COLLECTION_1, TEST_COLLECTION_2, TEST_COLLECTION_3


def test_no_fields_same():
	existing = list(find_existing_items(TEST_COLLECTION_1, TEST_COLLECTION_1))
	expected_existing = TEST_COLLECTION_1

	missing = list(find_missing_items(TEST_COLLECTION_1, TEST_COLLECTION_1))
	expected_missing = []

	assert existing == expected_existing
	assert missing == expected_missing


def test_no_fields_different():
	existing = list(find_existing_items(TEST_COLLECTION_2, TEST_COLLECTION_3))
	expected_existing = []

	missing = list(find_missing_items(TEST_COLLECTION_2, TEST_COLLECTION_3))
	expected_missing = TEST_COLLECTION_2

	assert existing == expected_existing
	assert missing == expected_missing


def test_no_fields_partial():
	existing = list(find_existing_items(TEST_COLLECTION_1, TEST_COLLECTION_2))
	expected_existing = [TEST_COLLECTION_1[0]]

	missing = list(find_missing_items(TEST_COLLECTION_1, TEST_COLLECTION_2))
	expected_missing = [TEST_COLLECTION_1[1]]

	assert existing == expected_existing
	assert missing == expected_missing


def test_fields_same():
	existing = list(
		find_existing_items(
			TEST_COLLECTION_1, TEST_COLLECTION_1, fields=['artist', 'album']
		)
	)
	expected_existing = TEST_COLLECTION_1

	missing = list(
		find_missing_items(
			TEST_COLLECTION_1, TEST_COLLECTION_1, fields=['artist', 'album']
		)
	)
	expected_missing = []

	assert existing == expected_existing
	assert missing == expected_missing


def test_fields_different():
	existing = list(
		find_existing_items(
			TEST_COLLECTION_2, TEST_COLLECTION_3, fields=['artist', 'album']
		)
	)
	expected_existing = []

	missing = list(
		find_missing_items(
			TEST_COLLECTION_2, TEST_COLLECTION_3, fields=['artist', 'album']
		)
	)
	expected_missing = TEST_COLLECTION_2

	assert existing == expected_existing
	assert missing == expected_missing


def test_fields_partial():
	existing = list(
		find_existing_items(
			TEST_COLLECTION_1, TEST_COLLECTION_2, fields=['artist', 'title']
		)
	)
	expected_existing = [TEST_COLLECTION_1[0]]

	missing = list(
		find_missing_items(
			TEST_COLLECTION_1, TEST_COLLECTION_2, fields=['artist', 'title']
		)
	)
	expected_missing = [TEST_COLLECTION_1[1]]

	assert existing == expected_existing
	assert missing == expected_missing


def test_default_field_map():
	existing = list(
		find_existing_items(
			TEST_COLLECTION_1, TEST_COLLECTION_2, fields=['tracknumber']
		)
	)
	expected_existing = [TEST_COLLECTION_1[0]]

	missing = list(
		find_missing_items(
			TEST_COLLECTION_1, TEST_COLLECTION_2, fields=['tracknumber']
		)
	)
	expected_missing = [TEST_COLLECTION_1[1]]

	assert existing == expected_existing
	assert missing == expected_missing


def test_default_field_map_no_exist():
	existing = list(
		find_existing_items(
			TEST_COLLECTION_1, TEST_COLLECTION_2,
			fields=['tracknumber', 'noexist']
		)
	)
	expected_existing = [TEST_COLLECTION_1[0]]

	missing = list(
		find_missing_items(
			TEST_COLLECTION_1, TEST_COLLECTION_2,
			fields=['tracknumber', 'noexist']
		)
	)
	expected_missing = [TEST_COLLECTION_1[1]]

	assert existing == expected_existing
	assert missing == expected_missing


def test_custom_field_map():
	existing = list(
		find_existing_items(
			TEST_COLLECTION_1, TEST_COLLECTION_2,
			fields=['tracknumber'], field_map={'tracknumber': 'track_number'}
		)
	)
	expected_existing = [TEST_COLLECTION_1[0]]

	missing = list(
		find_missing_items(
			TEST_COLLECTION_1, TEST_COLLECTION_2,
			fields=['tracknumber'], field_map={'tracknumber': 'track_number'}
		)
	)
	expected_missing = [TEST_COLLECTION_1[1]]

	assert existing == expected_existing
	assert missing == expected_missing


def test_custom_field_map_no_exist():
	existing = list(
		find_existing_items(
			TEST_COLLECTION_1, TEST_COLLECTION_2,
			fields=['tracknumber'],
			field_map={'tracknumber': 'track_number', 'noexist': 'no_exist'}
		)
	)
	expected_existing = [TEST_COLLECTION_1[0]]

	missing = list(
		find_missing_items(
			TEST_COLLECTION_1, TEST_COLLECTION_2,
			fields=['tracknumber'],
			field_map={'tracknumber': 'track_number', 'noexist': 'no_exist'}
		)
	)
	expected_missing = [TEST_COLLECTION_1[1]]

	assert existing == expected_existing
	assert missing == expected_missing
