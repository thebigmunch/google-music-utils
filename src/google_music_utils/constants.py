__all__ = [
	'CHARACTER_REPLACEMENTS',
	'FIELD_MAP',
	'TEMPLATE_PATTERNS',
]

from multidict import MultiDict

CHARACTER_REPLACEMENTS = {
	'\\': '-',
	'/': ',',
	':': '-',
	'*': 'x',
	'<': '[',
	'>': ']',
	'|': '!',
	'?': '',
	'"': "''",
}
"""dict: Mapping of invalid filepath characters with appropriate replacements."""

_FIELD_MAP_GROUPS = [
	('albumartist', 'album_artist', 'albumArtist'),
	('bpm', 'beatsPerMinute'),
	('date', 'year'),
	('discnumber', 'disc_number', 'discNumber'),
	('disctotal', 'total_disc_count', 'totalDiscCount'),
	('tracknumber', 'track_number', 'trackNumber'),
	('tracktotal', 'total_track_count', 'totalTrackCount'),
]
_FIELD_MAP = [
	(field, alias)
	for group in _FIELD_MAP_GROUPS
	for field in group
	for alias in group
	if field != alias
]

FIELD_MAP = MultiDict(_FIELD_MAP)
"""~multidict.MultiDict: Mapping of field name aliases."""

# TODO: Support other/more metadata field names.
TEMPLATE_PATTERNS = {
	'%album%': ['album'],
	'%albumartist%': ['albumartist', 'album_artist', 'albumArtist'],
	'%artist%': ['artist'],
	'%date%': ['date'],
	'%disc%': ['discnumber', 'disc_number', 'discNumber'],
	'%disc2%': ['discnumber', 'disc_number', 'discNumber'],
	'%discnumber%': ['discnumber', 'disc_number', 'discNumber'],
	'%discnumber2%': ['discnumber', 'disc_number', 'discNumber'],
	'%genre%': ['genre'],
	'%title%': ['title'],
	'%track%': ['tracknumber', 'track_number', 'trackNumber'],
	'%track2%': ['tracknumber', 'track_number', 'trackNumber'],
	'%tracknumber%': ['tracknumber', 'track_number', 'trackNumber'],
	'%tracknumber2%': ['tracknumber', 'track_number', 'trackNumber'],
}
"""dict: Mapping of template patterns to their metadata field names."""
