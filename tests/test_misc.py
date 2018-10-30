import os

import pytest
from google_music_utils.misc import suggest_filename, template_to_filepath


@pytest.mark.parametrize(
	'metadata, expected',
	[
		({'title': 'One Time', 'tracknumber': '1'}, '01 One Time'),
		({'title': 'One Time', 'track_number': '1'}, '01 One Time'),
		({'title': 'One Time', 'trackNumber': '1'}, '01 One Time'),
		({'title': 'One Time'}, '00 One Time')
	]
)
def test_misc_suggest_filename(metadata, expected):
	assert suggest_filename(metadata) == expected


@pytest.mark.parametrize(
	'template, metadata, expected',
	[
		(
			'%suggested%',
			{'artist': 'Marian Hill', 'album': 'Sway', 'tracknumber': '1', 'title': 'One Time'},
			'01 One Time'
		),
		(
			'%artist%/%album%/%tracknumber% - %title%',
			{'artist': 'Marian Hill', 'album': 'Sway', 'tracknumber': '1', 'title': 'One Time'},
			os.path.join('Marian Hill', 'Sway', '01 - One Time')
		),
		(
			'%artist%/%album%/%tracknumber% - %title%',
			{'artist': 'Marian Hill', 'album': 'Sway', 'tracknumber': '1/7', 'title': 'One Time'},
			os.path.join('Marian Hill', 'Sway', '01 - One Time')
		),
		# (
		# 	'C:/%artist%/%album%/%tracknumber% - %title%',
		# 	{'artist': 'Marian Hill', 'album': 'Sway', 'tracknumber': '1/7', 'title': 'One Time'},
		# 	os.path.join('C:\\', 'Marian Hill', 'Sway', '01 - One Time')
		# ),
		(
			'%artist%/%album%/%tracknumber% - %title%',
			{'artist': 'Marian Hill', 'album': 'Sway?', 'tracknumber': '1', 'title': 'One Time'},
			os.path.join('Marian Hill', 'Sway', '01 - One Time')
		),
		# (
		# 	'/%artist%/%album%/%tracknumber% - %title%',
		# 	{'artist': 'Marian Hill', 'album': 'Sway', 'tracknumber': '1', 'title': 'One Time'},
		# 	os.path.join('\\', 'Marian Hill', 'Sway', '01 - One Time')
		# )
	]
)
def test_misc_template_to_filepath_default_patterns(template, metadata, expected):
	assert template_to_filepath(template, metadata) == expected


@pytest.mark.parametrize(
	'template, metadata, expected',
	[
		(
			'%art%/%alb%/%track% - %tit%',
			{'artist': 'Marian Hill', 'album': 'Sway', 'tracknumber': '1', 'title': 'One Time'},
			os.path.join('Marian Hill', 'Sway', '01 - One Time')
		)
	]
)
def test_misc_template_to_filepath_custom_patterns(template, metadata, expected):
	assert template_to_filepath(
		template, metadata, template_patterns={
			'%alb%': 'album', '%art%': 'artist', '%tit%': 'title', '%track%': 'tracknumber'
		}
	) == expected
