1.0a8 (2016-07-21)
------------------

Breaking Changes:

- Change ROBOT_LIBRARY_SCOPE to 'GLOBAL'. It does not make sense to fire up
  webpack for every single test.
  [timo]


1.0a7 (2016-07-19)
------------------

Bugfixes:

- Do not log the webpack path.
  [timo]


1.0a6 (2016-07-18)
------------------

Bugfixes:

- Allow to use 'Start Webpack' keyword without a debug attribute set. This
  fixes https://github.com/kitconcept/robotframework-webpack/issues/2.
  [timo]


1.0a5 (2016-07-13)
------------------

New Features:

- Add 'webpack_bin_path' param to 'Start Webpack' keyword.
  [timo]


1.0a4 (2016-07-13)
------------------

Breaking Changes:

- Move all arguments from WebpackLibrary import to 'Start Webpack' keyword.
  [timo]

Bugfixes:

- Remove requests from dependencies.
  [timo]

- Fix package keywords.
  [timo]


1.0a3 (2016-07-13)
------------------

Bugfixes:

- Fix content_base param.
  [timo]

- Log OSErrors when calling webpack.
  [timo]


1.0a2 (2016-07-13)
------------------

New Features:

- Add config parameter to WebpackLibrary.
  [timo]

1.0a1 (2016-07-12)
------------------

- Initial release.
  [timo]
