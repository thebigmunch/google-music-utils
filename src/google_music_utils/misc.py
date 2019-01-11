__all__ = ['suggest_filename', 'template_to_filepath']

import re
from pathlib import Path

from .constants import CHARACTER_REPLACEMENTS, TEMPLATE_PATTERNS
from .utils import list_to_single_value


def _replace_invalid_characters(filepath):
	for char in CHARACTER_REPLACEMENTS:
		filepath = filepath.replace(char, CHARACTER_REPLACEMENTS[char])

	return filepath


def suggest_filename(metadata):
	"""Generate a filename like Google for a song based on metadata.

	Parameters:
		metadata (~collections.abc.Mapping): A metadata dict.

	Returns:
		str: A filename string without an extension.
	"""

	if 'title' in metadata and 'track_number' in metadata:  # Music Manager.
		suggested_filename = f"{metadata['track_number']:0>2} {metadata['title']}"
	elif 'title' in metadata and 'trackNumber' in metadata:  # Mobile.
		suggested_filename = f"{metadata['trackNumber']:0>2} {metadata['title']}"
	elif 'title' in metadata and 'tracknumber' in metadata:  # audio-metadata/mutagen.
		track_number = list_to_single_value(metadata['tracknumber'])
		title = list_to_single_value(metadata['title'])

		suggested_filename = f"{track_number:0>2} {title}"
	else:
		suggested_filename = f"00 {list_to_single_value(metadata.get('title', ['']))}"

	return _replace_invalid_characters(suggested_filename)


def _split_track_number(field):
	match = re.match(r'(\d+)(?:/\d+)?', field)

	return match.group(1) if match else field


def template_to_filepath(template, metadata, template_patterns=None):
	"""Create directory structure and file name based on metadata template.

	Note:

	A template meant to be a base directory for suggested
	names should have a trailing slash or backslash.

	Parameters:
		template (str or ~os.PathLike): A filepath which can include template patterns as defined by :param template_patterns:.

		metadata (~collections.abc.Mapping): A metadata dict.

		template_patterns (~collections.abc.Mapping): A dict of ``pattern: field`` pairs used to replace patterns with metadata field values.
			Default: :const:`~google_music_utils.constants.TEMPLATE_PATTERNS`

	Returns:
		~pathlib.Path: A filepath.
	"""

	path = Path(template)

	if template_patterns is None:
		template_patterns = TEMPLATE_PATTERNS

	suggested_filename = suggest_filename(metadata)

	if (
		path == Path.cwd()
		or path == Path('%suggested%')
	):
		filepath = Path(suggested_filename)
	elif any(template_pattern in path.parts for template_pattern in template_patterns):
		if template.endswith(('/', '\\')):
			template += suggested_filename

		path = Path(template.replace('%suggested%', suggested_filename))

		parts = []
		for part in path.parts:
			if part == path.anchor:
				parts.append(part)
			else:
				for key in template_patterns:
					if key in part and template_patterns[key] in metadata:
						# Force track number to be zero-padded to 2 digits.
						if any(
							template_patterns[key] == tracknumber_field for tracknumber_field in ['tracknumber', 'track_number']
						):
							track_number = _split_track_number(str(list_to_single_value(metadata[template_patterns[key]])))
							metadata[template_patterns[key]] = track_number.zfill(2)

						part = part.replace(
							key,
							list_to_single_value(
								metadata[template_patterns[key]]
							)
						)

				parts.append(_replace_invalid_characters(part))

		filepath = Path(*parts)
	elif '%suggested%' in template:
		filepath = Path(template.replace('%suggested%', suggested_filename))
	elif template.endswith(('/', '\\')):
		filepath = path / suggested_filename
	else:
		filepath = path

	return filepath
