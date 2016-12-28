import pytest
from google_music_utils.utils import list_to_single_value, normalize_value


@pytest.mark.parametrize(
	'value, expected',
	[
		('Beck', 'Beck'),
		(['Beck', 'Beck Hansen'], 'Beck')
	]
)
def test_list_to_single_value(value, expected):
	assert list_to_single_value(value) == expected


@pytest.mark.parametrize(
	'metadata, expected',
	[
		('Beck', 'beck'),
		('1/10', '1'),  # Remove "/<totaltracks>" from track number.
		('01', '1'),  # Remove leading zero(s) from track number.
		('1..', '1'),  # Remove dots from track number.
		('!!!', ''),  # Remove leading non-word characters.
		('The Streets', 'streets'),  # Remove leading "the".
		('  Beck', 'beck'),  # Remove leading spaces.
		('Beck  ', 'beck'),  # Remove trailing spaces.
		('Marian  Hill', 'marian hill')  # Reduce multiple spaces to a single space.
	]
)
def test_normalize_value(metadata, expected):
	assert normalize_value(metadata) == expected
