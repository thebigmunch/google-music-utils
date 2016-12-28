import time
from uuid import uuid4

import pytest
from google_music_utils.metadata import (
	from_gm_timestamp, gm_timestamp, is_album_id, is_artist_id,
	is_podcast_episode_id, is_podcast_series_id,
	is_store_song_id, is_uuid, to_gm_timestamp
)

album_id = 'Bklw2nqk2axv2cdjhmblppa2c6i'
artist_id = 'Adx4m3rvetjs5bs3jrbglwkt46i'
podcast_episode_id = 'Dwe6ocaevhllxngileqizmhv4le'
podcast_series_id = 'Iliyrhelw74vdqrro77kq2vrdhy'
store_song_id = 'Tqwfxchruvu547vwfqvm6vw6gse'
uuid_ = str(uuid4())


def test_metadata_gm_timestamp():
	gm_stamp = gm_timestamp()
	timestamp = int(time.time())
	expected_len = len(str(timestamp)) + 6

	assert isinstance(gm_stamp, int) and len(str(gm_stamp)) == expected_len
	assert timestamp == from_gm_timestamp(to_gm_timestamp(timestamp))


@pytest.mark.parametrize(
	'item_id, expected',
	[
		(album_id, True),
		(artist_id, False),
		(podcast_episode_id, False),
		(podcast_series_id, False),
		(store_song_id, False),
		(uuid_, False)
	]
)
def test_metadata_is_album_id(item_id, expected):
	assert is_album_id(item_id) is expected


@pytest.mark.parametrize(
	'item_id, expected',
	[
		(album_id, False),
		(artist_id, True),
		(podcast_episode_id, False),
		(podcast_series_id, False),
		(store_song_id, False),
		(uuid_, False)
	]
)
def test_metadata_is_artist_id(item_id, expected):
	assert is_artist_id(item_id) is expected


@pytest.mark.parametrize(
	'item_id, expected',
	[
		(album_id, False),
		(artist_id, False),
		(podcast_episode_id, True),
		(podcast_series_id, False),
		(store_song_id, False),
		(uuid_, False)
	]
)
def test_metadata_is_podcast_episode_id(item_id, expected):
	assert is_podcast_episode_id(item_id) is expected


@pytest.mark.parametrize(
	'item_id, expected',
	[
		(album_id, False),
		(artist_id, False),
		(podcast_episode_id, False),
		(podcast_series_id, True),
		(store_song_id, False),
		(uuid_, False)
	]
)
def test_metadata_is_podcast_series_id(item_id, expected):
	assert is_podcast_series_id(item_id) is expected


@pytest.mark.parametrize(
	'item_id, expected',
	[
		(album_id, False),
		(artist_id, False),
		(podcast_episode_id, False),
		(podcast_series_id, False),
		(store_song_id, True),
		(uuid_, False)
	]
)
def test_metadata_is_store_song_id(item_id, expected):
	assert is_store_song_id(item_id) is expected


@pytest.mark.parametrize(
	'item_id, expected',
	[
		(album_id, False),
		(artist_id, False),
		(podcast_episode_id, False),
		(podcast_series_id, False),
		(store_song_id, False),
		(uuid_, True)
	]
)
def test_metadata_is_uuid(item_id, expected):
	assert is_uuid(item_id) is expected
