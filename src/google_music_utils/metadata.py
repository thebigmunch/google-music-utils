__all__ = [
	'gm_timestamp', 'from_gm_timestamp', 'to_gm_timestamp',
	'is_album_id', 'is_artist_id', 'is_podcast_episode_id',
	'is_podcast_series_id', 'is_store_song_id', 'is_uuid'
]

import re
import time

_uuid_re = re.compile(r'^[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}$')


def gm_timestamp():
	"""Generate a timestamp in microseconds."""

	return int(time.time() * 1000000)


def from_gm_timestamp(timestamp):
	"""Convert timestamp in microseconds to timestamp in seconds."""

	return int(timestamp / 1000000)


def to_gm_timestamp(timestamp):
	"""Convert timestamp in seconds to timestamp in microseconds."""

	return int(timestamp * 1000000)


def is_album_id(item_id):
	"""Validate if ID is in the format of a Google Music album ID."""

	return len(item_id) == 27 and item_id.startswith('B')


def is_artist_id(item_id):
	"""Validate if ID is in the format of a Google Music artist ID."""

	return len(item_id) == 27 and item_id.startswith('A')


def is_podcast_episode_id(item_id):
	"""Validate if ID is in the format of a Google Music podcast episode ID."""

	return len(item_id) == 27 and item_id.startswith('D')


def is_podcast_series_id(item_id):
	"""Validate if ID is in the format of a Google Music series ID."""

	return len(item_id) == 27 and item_id.startswith('I')


def is_store_song_id(item_id):
	"""Validate if ID is in the format of a Google Music store song ID."""

	return len(item_id) == 27 and item_id.startswith('T')


def is_uuid(item_id):
	"""Validate if ID is in the format of a UUID (used for library song IDs)."""

	return bool(_uuid_re.match(item_id))
