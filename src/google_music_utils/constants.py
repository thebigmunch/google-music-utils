__all__ = ['CHARACTER_REPLACEMENTS', 'FIELD_MAP', 'TEMPLATE_PATTERNS']

from multidict import MultiDict

CHARACTER_REPLACEMENTS = {
	'\\': '-', '/': ',', ':': '-', '*': 'x', '<': '[',
	'>': ']', '|': '!', '?': '', '"': "''"
}
"""dict: Mapping of invalid filepath characters with appropriate replacements."""

_FIELD_MAP_GROUPS = [
	('albumartist', 'album_artist', 'albumArtist'), ('bpm', 'beatsPerMinute'), ('date', 'year'),
	('discnumber', 'disc_number', 'discNumber'), ('disctotal', 'total_disc_count', 'totalDiscCount'),
	('tracknumber', 'track_number', 'trackNumber'), ('tracktotal', 'total_track_count', 'totalTrackCount')
]
_FIELD_MAP = [(field, alias) for group in _FIELD_MAP_GROUPS for field in group for alias in group if field != alias]

FIELD_MAP = MultiDict(_FIELD_MAP)

# TODO: Support other/more metadata field names.
# TODO: Support multiple field names per template pattern.
TEMPLATE_PATTERNS = {
	'%artist%': 'artist', '%title%': 'title', '%tracknumber%': 'tracknumber',
	'%album%': 'album', '%date%': 'date', '%genre%': 'genre',
	'%albumartist%': 'albumartist', '%discnumber%': 'discnumber'
}
"""dict: Mapping of template patterns to their audio-metadata field name."""
