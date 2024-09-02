# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]

### Added

- Added a `rule34Py.iter_search()` method that returns a Post search iterator that transparently handles pagination. (#20)
- Added a `rule34Py._get()` method to handle HTTP GET requests from the servers. This logic was previously duplicated within most of the client's methods. (#20)
- Added a `rule34Py.tag_map()` method which parses and returns the top 100 global tags (that was previously being returned from the `tagmap()` method.) (#20)
- Added a `rule34Py.top_tags()` method, that parses the global Top-100 tags from the toptags page (like the deprecated `tagmap()` method.) (#20)
- Added a `rule34Py.user_agent` class variable, that users can change to modify the client's User-Agent. (#20)

### Changed

- Began migrating the client's User-Agent string into a client-scope variable (from the module), so that users can alter it if they wish.
- `rule34Py` no longer inherits from the `Exception` class.

### Deprecated

- Announced deprecation of the `rule34Py.rule34Py.version` property. Users should check the value of the module-scope `rule34Py.version` variable instead.  (#20)
- Announced deprecation of the `rule34Py.rule34Py.tagmap()` method. Users should either call `rule34Py.top_tags()` to continue getting the Top-100 tags chart, or `rule34Py.tag_map()` to get the new Tag Map data points.  (#20)

### Removed

- Removed the `deleted` and `ignore_max_limit` parameters from the `rule34Py.search()` method. Neither worked and only ever returned an exception. (#20)
- Removed the `limit` parameter from the `rule34Py.icame()` method, as it did nothing. Users are directed to use list slicing instead. (#20)

### Fixed
### Security


## [2.0.0] - 2024-09-02

### Added

-  Added an autotesting suite based on `pytest` and `Responses`. (#16)
-  Added a NOTICE.md file to tack third party license inclusions. (#16)

### Changed

- Updated the README quickstart instructions to avoid dead object references. (#16)
- Switched the canonical project build framework from `setup.py` to `pyproject.toml`. (#18)

### Removed

- Removed the `rule34Py.stats` feature, as it was removed from the upstream Rule34 APIs. (#17)
- Removed the legacy `rule34Py_old` module, as it is no longer functional. (#17)

### Fixed

- Fixed the `rule34Py.get_pool()` method using the wrong API url. (#16)


## [1.4.11] - 2023-12-25

### Changed

- Updated and refreshed project documentation. (#13)

### Fixed

- Fixed the `rule34Py.random_post()` method using the wrong API url. (#4, #5)
- Fixed an IndexError in the `rule34.random_post()` method. (#8)


## [1.4.10] - 2023-02-22
### Added
- `from_json` to Post class
- `preview` field to Post class
- `thumbnail` field to Post class
- `sample` field to Post class
- `video` field to Post class
- `directory` field to Post class
- `change` field to Post class
- `content_type` field to Post class
- example files

### Changed
- changed how `search` and `get_post` are creating post objects


## [1.4.9] - 2022-12-26
### Fixed
- Fixed bug where 'search' function didn't used value parameter of 'page_id'


## [1.4.8] - 2022-12-01
### Added
- new class for TopMap

### Changed
- made [README.md](https://github.com/b3yc0d3/rule34Py#readme) look nicer
- updated code snippet
- updated documentation
- `rule34Py.tagmap()` now retuns list of *TopTag*s

### Fixed
- fixed bug where random number could exceed array length of Random
- typos in some markdown files


## [1.4.7] - 2022-09-22
### Changed
- `RANDOM_POST` URI now uses '**&#95;&#95;base&#95;url&#95;&#95;**' instead of '**&#95;&#95;api&#95;url&#95;&#95;**' ( by talbaskin.business@gmail.com )

## [1.4.5] - 2022-04-25
### Changed
- added to function `search` additional error handling
- updated DOCS
- updated rule34.xxx api url

## [1.4.4] - 2022-04-11
### Changed
- search function, added new parameter "ignore_max_limit"
- updated Docs
- author email

## [1.4.3] - 2022-01-16
### Changed
- setuppy min versions

## [1.4.2] - 2021-11-18
### Added
- "tagmap" function (and docs for it)

### Changed
- updated code snippet

## [1.4.1] - 2021-11-10
### Added
- "get_pool" Function (and docs for it)

### Changed
- relative links to absolute links in all readme files

## [1.4.0] - 2021-11-07
### Added
- "search" Function
- "get_comments" Functon
- "get_post" Functon
- "icame" Functon (and docs for it)
- "random_post" Functon
- docs for every Object (an old doc for 1.3.38 and below)
- new code snippet/example

### Changed
- Fixed [bug](https://github.com/b3yc0d3/rule34Py/issues/2#issuecomment-902728779)

### Changed
- updated README

## [1.3.20] - 2021-08-20
### Changed
- fixed [bug](https://github.com/b3yc0d3/rule34Py/issues/2)
- "src/rule34Py.py"

## [1.3.20] - 2021-08-02
### Changed
- "random" Functon
- "README.md" upated documentation

## [0.0.1] - 2021-05-06
### Added
- "search" Function
- "getCommets" Function
- "getAccount" Function
- "getPost" Function
- "getFavorites" Function
- LINCENSE.txt
- setup.py
- src/rule34Py.py
- src/test.xml
- src/http_client.py
- src/test.xml
- debug.py
- setup.py
