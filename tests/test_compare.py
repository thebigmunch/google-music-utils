# TODO: Add metadata normalization tests.

from google_music_utils import compare_item_collections

from .fixtures import TEST_COLLECTION_1, TEST_COLLECTION_2, TEST_COLLECTION_3


def test_compare_no_fields_same():
	result = list(compare_item_collections(TEST_COLLECTION_1, TEST_COLLECTION_1))
	expected = []

	assert result == expected


def test_compare_no_fields_different():
	result = list(compare_item_collections(TEST_COLLECTION_2, TEST_COLLECTION_3))
	expected = TEST_COLLECTION_2

	assert result == expected


def test_compare_no_fields_partial():
	result = list(compare_item_collections(TEST_COLLECTION_1, TEST_COLLECTION_2))
	expected = [TEST_COLLECTION_1[1]]

	assert result == expected


def test_compare_fields_same():
	result = list(compare_item_collections(TEST_COLLECTION_1, TEST_COLLECTION_1, fields=['artist', 'album']))
	expected = []

	assert result == expected


def test_compare_fields_different():
	result = list(compare_item_collections(TEST_COLLECTION_2, TEST_COLLECTION_3, fields=['artist', 'album']))
	expected = TEST_COLLECTION_2

	assert result == expected


def test_compare_fields_partial():
	result = list(compare_item_collections(TEST_COLLECTION_1, TEST_COLLECTION_2, fields=['artist', 'title']))
	expected = [TEST_COLLECTION_1[1]]

	assert result == expected


def test_compare_default_field_map():
	result = list(compare_item_collections(TEST_COLLECTION_1, TEST_COLLECTION_2, fields=['tracknumber']))
	expected = [TEST_COLLECTION_1[1]]

	assert result == expected


def test_compare_default_field_map_no_exist():
	result = list(compare_item_collections(TEST_COLLECTION_1, TEST_COLLECTION_2, fields=['tracknumber', 'noexist']))
	expected = [TEST_COLLECTION_1[1]]

	assert result == expected


def test_compare_custom_field_map():
	result = list(compare_item_collections(TEST_COLLECTION_1, TEST_COLLECTION_2, fields=['tracknumber'], field_map={'tracknumber': 'track_number'}))
	expected = [TEST_COLLECTION_1[1]]

	assert result == expected


def test_compare_custom_field_map_no_exist():
	result = list(compare_item_collections(TEST_COLLECTION_1, TEST_COLLECTION_2, fields=['tracknumber'], field_map={'tracknumber': 'track_number', 'noexist': 'no_exist'}))
	expected = [TEST_COLLECTION_1[1]]

	assert result == expected
