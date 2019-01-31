import sys
from pathlib import Path

import pytest
from audio_metadata import Tags
from google_music_utils.misc import suggest_filename, template_to_filepath


@pytest.mark.parametrize(
	'metadata, expected',
	[
		({'title': 'One Time', 'tracknumber': '1'}, '01 One Time'),
		({'title': 'One Time', 'tracknumber': '1/7'}, '01 One Time'),
		(Tags(**{'title': 'One Time', 'tracknumber': '1/7'}), '01 One Time'),
		({'title': 'One Time', 'track_number': '1'}, '01 One Time'),
		({'title': 'One Time', 'trackNumber': '1'}, '01 One Time'),
		({'title': 'One Time'}, '00 One Time'),
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
			Path('01 One Time')
		),
		(
			'%artist%/%album%/%tracknumber% - %title%',
			{'artist': 'Marian Hill', 'album': 'Sway', 'tracknumber': '1', 'title': 'One Time'},
			Path('Marian Hill', 'Sway', '1 - One Time')
		),
		(
			'%artist%/%album%/%tracknumber2% - %title%',
			{'artist': 'Marian Hill', 'album': 'Sway', 'tracknumber': '1', 'title': 'One Time'},
			Path('Marian Hill', 'Sway', '01 - One Time')
		),
		(
			'%artist%/%album%/%tracknumber% - %title%',
			{'artist': 'Marian Hill', 'album': 'Sway', 'tracknumber': '1/7', 'title': 'One Time'},
			Path('Marian Hill', 'Sway', '1 - One Time')
		),
		(
			'%artist%/%album%/%tracknumber% - %title%',
			{'artist': 'Marian Hill', 'album': 'Sway?', 'tracknumber': '1', 'title': 'One Time'},
			Path('Marian Hill', 'Sway', '1 - One Time')
		),
		(
			'/%artist%/%album%/%tracknumber% - %title%',
			{'artist': 'Marian Hill', 'album': 'Sway', 'tracknumber': '1', 'title': 'One Time'},
			Path('/', 'Marian Hill', 'Sway', '1 - One Time')
		),
		(
			'C:/%artist%/%album%/%tracknumber% - %title%',
			{'artist': 'Marian Hill', 'album': 'Sway', 'tracknumber': '1/7', 'title': 'One Time'},
			Path('C:\\', 'Marian Hill', 'Sway', '1 - One Time')
		),
		(
			'/%artist%/%album%/%tracknumber% - %title%',
			{'artist': 'Marian Hill', 'album': 'Sway', 'tracknumber': '1', 'title': 'One Time'},
			Path('\\', 'Marian Hill', 'Sway', '1 - One Time')
		),
		(
			'%artist%/%album%/',
			{'artist': 'Marian Hill', 'album': 'Sway?', 'tracknumber': '1', 'title': 'One Time'},
			Path('Marian Hill', 'Sway', '01 One Time')
		),
		(
			'Marian Hill/Sway/%suggested%',
			{'artist': 'Marian Hill', 'album': 'Sway?', 'tracknumber': '1', 'title': 'One Time'},
			Path('Marian Hill', 'Sway', '01 One Time')
		),
		(
			'Marian Hill/Sway/',
			{'artist': 'Marian Hill', 'album': 'Sway?', 'tracknumber': '1', 'title': 'One Time'},
			Path('Marian Hill', 'Sway', '01 One Time')
		),
		(
			'Marian Hill/Sway/01 One Time',
			{'artist': 'Marian Hill', 'album': 'Sway?', 'tracknumber': '1', 'title': 'One Time'},
			Path('Marian Hill', 'Sway', '01 One Time')
		),
	]
)
def test_misc_template_to_filepath_default_patterns(template, metadata, expected):
	if not sys.platform.startswith('win'):
		if template.startswith('C:/'):
			pytest.skip("Skipping Windows-only test.")

		if template.startswith('/') and str(expected).startswith('\\'):
			pytest.skip("Skipping Windows-only test.")
	elif template.startswith('/') and str(expected).startswith('/'):
		pytest.skip("Skipping non-Windows test.")

	assert template_to_filepath(template, metadata) == expected


@pytest.mark.parametrize(
	'template, metadata, expected',
	[
		(
			'%art%/%alb%/%tracknum% - %tit%',
			{'artist': 'Marian Hill', 'album': 'Sway', 'tracknumber': '1', 'title': 'One Time'},
			Path('Marian Hill', 'Sway', '1 - One Time')
		),
		(
			'%art%/%alb%/%tracknum2% - %tit%',
			{'artist': 'Marian Hill', 'album': 'Sway', 'tracknumber': '1', 'title': 'One Time'},
			Path('Marian Hill', 'Sway', '01 - One Time')
		)
	]
)
def test_misc_template_to_filepath_custom_patterns(template, metadata, expected):
	assert template_to_filepath(
		template, metadata, template_patterns={
			'%alb%': ['album'],
			'%art%': ['artist'],
			'%tit%': ['title'],
			'%tracknum%': ['tracknumber'],
			'%tracknum2%': ['tracknumber']
		}
	) == expected
