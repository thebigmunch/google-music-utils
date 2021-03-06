# Change Log

Notable changes to this project based on the [Keep a Changelog](https://keepachangelog.com) format.
This project adheres to [Semantic Versioning](https://semver.org).


## [Unreleased](https://github.com/thebigmunch/google-music-utils/tree/master)

[Commits](https://github.com/thebigmunch/google-music-utils/compare/2.5.0...master)


## [2.5.0](https://github.com/thebigmunch/google-music-utils/releases/tag/2.5.0) (2020-05-18)

[Commits](https://github.com/thebigmunch/google-music-utils/compare/2.4.0...2.5.0)

### Changed

* Cast timestamp argument to int in timestamp functions.


## [2.4.0](https://github.com/thebigmunch/google-music-utils/releases/tag/2.4.0) (2020-05-01)

[Commits](https://github.com/thebigmunch/google-music-utils/compare/2.3.0...2.4.0)

### Changed

* Revert "Use importlib.metadata to dynamically populate module metadata".


## [2.3.0](https://github.com/thebigmunch/google-music-utils/releases/tag/2.3.0) (2020-04-08)

[Commits](https://github.com/thebigmunch/google-music-utils/compare/2.2.1...2.3.0)

### Changed

* Update dependency versions.


## [2.2.1](https://github.com/thebigmunch/google-music-utils/releases/tag/2.2.1) (2019-10-18)

[Commits](https://github.com/thebigmunch/google-music-utils/compare/2.2.0...2.2.1)

### Fixed

* Catch exceptions when trying to load files with audio-metadata.


## [2.2.0](https://github.com/thebigmunch/google-music-utils/releases/tag/2.2.0) (2019-07-22)

[Commits](https://github.com/thebigmunch/google-music-utils/compare/2.1.0...2.2.0)

### Changed

* Update audio-metadata dependency version.


## [2.1.0](https://github.com/thebigmunch/google-music-utils/releases/tag/2.1.0) (2019-02-01)

[Commits](https://github.com/thebigmunch/google-music-utils/compare/2.0.1...2.1.0)

### Added

* Support for field maps in filtering.

### Changed

* ``TEMPLATE_PATTERNS`` now supports multiple fields per pattern.
* ``template_to_filepath no longer forces zero-padding of track/disc numbers.


## [2.0.1](https://github.com/thebigmunch/google-music-utils/releases/tag/2.0.1) (2019-01-16)

[Commits](https://github.com/thebigmunch/google-music-utils/compare/2.0.0...2.0.1)

### Fixed

* Split track number in ``suggest_filename`` for audio-metadata/mutagen metadata.


## [2.0.0](https://github.com/thebigmunch/google-music-utils/releases/tag/2.0.0) (2019-01-15)

[Commits](https://github.com/thebigmunch/google-music-utils/compare/1.1.1...2.0.0)

### Changed

* ``template_to_filepath`` now returns a ``pathlib.Path`` object instead of a ``str``.

### Removed

* ``compare_item_collections``


## [1.1.1](https://github.com/thebigmunch/google-music-utils/releases/tag/1.1.1) (2018-11-28)

[Commits](https://github.com/thebigmunch/google-music-utils/compare/1.1.0...1.1.1)

### Fixed

* Forgot to update ``audio-metadata`` dependency in pyproject.toml.


## [1.1.0](https://github.com/thebigmunch/google-music-utils/releases/tag/1.1.0) (2018-10-28)

[Commits](https://github.com/thebigmunch/google-music-utils/compare/1.0.0...1.1.0)

### Added

* ``find_existing_items`` for finding items common to two item collections.
* ``normalize_func`` parameter to compare module functions to allow custom
	field value normalization when ``normalize_values`` is ``True``.
	The default normalization function remains the same.

### Changed

* Rename ``compare_item_collections`` to ``find_missing_items``.
	``compare_item_collections`` alias added for backward compatibility.
* ``str.casefold()`` is now used to normalize metadata rather than
	``str.lower()``. This is friendlier to non-English language.

### Deprecated

* ``compare_item_collections`` is deprecated for removal in a future release.

### Fixed

* Properly support audio-metadata.


## [1.0.0](https://github.com/thebigmunch/google-music-utils/releases/tag/1.0.0) (2018-10-19)

[Commits](https://github.com/thebigmunch/google-music-utils/commit/d466a8cb75041c1d1f6add1a999bfd1e25e73b0c)

* Initial release.
