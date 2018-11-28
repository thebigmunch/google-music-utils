# Change Log

Notable changes to this project based on the [Keep a Changelog](https://keepachangelog.com) format.
This project adheres to [Semantic Versioning](https://semver.org).


## [Unreleased](https://github.com/thebigmunch/google-music-utils/tree/master)

[Commits](https://github.com/thebigmunch/google-music-utils/compare/1.1.1...master)


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
