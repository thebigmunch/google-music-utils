__all__ = ['suggest_filename', 'template_to_filepath']

import os
import re

from .constants import CHARACTER_REPLACEMENTS, TEMPLATE_PATTERNS
from .utils import list_to_single_value


def suggest_filename(metadata):
	"""Generate a filename like Google for a song based on metadata.

	Parameters:
		metadata (dict): A metadata dict.

	Returns:
		str: A filename string without an extension.
	"""

	metadata = {k: list_to_single_value(v) for k, v in metadata.items()}

	if 'title' in metadata and 'track_number' in metadata:  # Music Manager.
		suggested_filename = f"{metadata['track_number']:0>2} {metadata['title']}"
	elif 'title' in metadata and 'trackNumber' in metadata:  # Mobile.
		suggested_filename = f"{metadata['trackNumber']:0>2} {metadata['title']}"
	elif 'title' in metadata and 'tracknumber' in metadata:  # Mutagen.
		suggested_filename = f"{metadata['tracknumber']:0>2} {metadata['title']}"
	else:
		suggested_filename = f"00 {metadata.get('title', '')}"

	return suggested_filename


def _split_track_number(field):
	match = re.match(r'(\d+)(?:/\d+)?', field)

	return match.group(1) if match else field


# TODO: Revisit template_to_filepath.
def _replace_template_patterns(template, metadata, template_patterns):
	drive, path = os.path.splitdrive(template)
	parts = []

	while True:
		newpath, tail = os.path.split(path)

		if newpath == path:
			break

		parts.append(tail)
		path = newpath

	parts.reverse()

	for i, part in enumerate(parts):
		for key in template_patterns:
			if key in part and template_patterns[key] in metadata:
				# Force track number to be zero-padded to 2 digits.
				if any(
					template_patterns[key] == tracknumber_field for tracknumber_field in ['tracknumber', 'track_number']
				):
					track_number = list_to_single_value(_split_track_number(str(metadata[template_patterns[key]])))
					metadata[template_patterns[key]] = track_number.zfill(2)

				parts[i] = parts[i].replace(key, metadata[template_patterns[key]])

		for char in CHARACTER_REPLACEMENTS:
			if char in parts[i]:
				parts[i] = parts[i].replace(char, CHARACTER_REPLACEMENTS[char])

	if os.path.isabs(template):
		if drive:
			filepath = os.path.join(drive, os.sep, *parts)
		else:
			filepath = os.path.join(os.sep, *parts)
	else:
		filepath = os.path.join(*parts)

	return filepath


def template_to_filepath(template, metadata, template_patterns=None):
	"""Create directory structure and file name based on metadata template.

	Parameters:
		template (str): A filepath which can include template patterns as defined by :param template_patterns:.

		metadata (dict): A metadata dict.

		template_patterns (dict): A dict of ``pattern: field`` pairs used to replace patterns with metadata field values.
			Default: :const:`~google_music_utils.constants.TEMPLATE_PATTERNS`

	Returns:
		str: A filepath.
	"""

	if template_patterns is None:
		template_patterns = TEMPLATE_PATTERNS

	metadata = {k: list_to_single_value(v) for k, v in metadata.items()}
	assert isinstance(metadata, dict)

	suggested_filename = suggest_filename(metadata)

	if template == os.getcwd() or template == '%suggested%':
		filepath = suggested_filename
	else:
		t = template.replace('%suggested%', suggested_filename)
		filepath = _replace_template_patterns(t, metadata, template_patterns)

	return filepath
