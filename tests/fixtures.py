from pathlib import Path

from audio_metadata import Format


TEST_MAPPING_1 = {
	'album': 'Black Holes and Revelations',
	'artist': ['Muse'],
	'title': ['Take a Bow'],
	'track_number': 1,
	'year': 2006
}

TEST_MAPPING_2 = {
	'album': 'Black Holes and Revelations',
	'artist': 'Muse',
	'title': 'Starlight',
	'track_number': 2,
	'year': 2006
}

TEST_MAPPING_3 = {
	'album': 'Odelay',
	'artist': 'Beck',
	'title': 'The New Pollution',
	'track_number': 4,
	'year': 1996
}

TEST_MAPPING_ITEMS_1 = [
	TEST_MAPPING_1,
	TEST_MAPPING_2
]

TEST_MAPPING_ITEMS_2 = [
	TEST_MAPPING_1
]

TEST_MAPPING_ITEMS_3 = [
	TEST_MAPPING_3
]


TEST_FORMAT_1 = Format._load(b'')
TEST_FORMAT_1.tags.update(TEST_MAPPING_1)

TEST_FORMAT_2 = Format._load(b'')
TEST_FORMAT_2.tags.update(TEST_MAPPING_2)

TEST_FORMAT_3 = Format._load(b'')
TEST_FORMAT_3.tags.update(TEST_MAPPING_3)

TEST_FORMAT_ITEMS_1 = [
	TEST_FORMAT_1,
	TEST_FORMAT_2
]

TEST_FORMAT_ITEMS_2 = [
	TEST_FORMAT_1
]

TEST_FORMAT_ITEMS_3 = [
	TEST_FORMAT_3
]


TEST_PATH_1 = Path(__file__).parent / 'test_files' / 'test_file_1.flac'
TEST_PATH_2 = Path(__file__).parent / 'test_files' / 'test_file_2.flac'
TEST_PATH_3 = Path(__file__).parent / 'test_files' / 'test_file_3.flac'

TEST_PATH_ITEMS_1 = [
	TEST_PATH_1,
	TEST_PATH_2
]

TEST_PATH_ITEMS_2 = [
	TEST_PATH_1
]

TEST_PATH_ITEMS_3 = [
	TEST_PATH_3
]
