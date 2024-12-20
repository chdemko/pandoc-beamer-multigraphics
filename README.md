Installation
============

[![Python package](https://img.shields.io/github/actions/workflow/status/chdemko/pandoc-beamer-multigraphics/python-package.yml?logo=github&branch=develop)](https://github.com/chdemko/pandoc-beamer-multigraphics/actions/workflows/python-package.yml)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-beamer-multigraphics/develop.svg?logo=Codecov&logoColor=white)](https://coveralls.io/github/chdemko/pandoc-beamer-multigraphics?branch=develop)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-beamer-multigraphics.svg?logo=scrutinizer)](https://scrutinizer-ci.com/g/chdemko/pandoc-beamer-multigraphics/)
[![Code Climate](https://img.shields.io/codeclimate/maintainability/chdemko/pandoc-beamer-multigraphics?logo=codeclimate&barnch=develop)](https://codeclimate.com/github/chdemko/pandoc-beamer-multigraphics/)
[![CodeFactor](https://img.shields.io/codefactor/grade/github/chdemko/pandoc-beamer-multigraphics/develop.svg?logo=codefactor)](https://www.codefactor.io/repository/github/chdemko/pandoc-beamer-multigraphics)
[![Codacy](https://img.shields.io/codacy/grade/1f76fd0c0e784f6ea1d96e40d7927f55.svg?logo=codacy)](https://app.codacy.com/gh/chdemko/pandoc-beamer-multigraphics/dashboard)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-beamer-multigraphics.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-beamer-multigraphics/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-beamer-multigraphics.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-beamer-multigraphics/)
[![License](https://img.shields.io/pypi/l/pandoc-beamer-multigraphics.svg?logo=pypi&logoColor=white)](https://raw.githubusercontent.com/chdemko/pandoc-beamer-multigraphics/develop/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-numbering?logo=pypi&logoColor=white)](https://pepy.tech/project/pandoc-beamer-multigraphics)
[![Development Status](https://img.shields.io/pypi/status/pandoc-beamer-multigraphics.svg?pypi&logoColor=white)](https://pypi.org/project/pandoc-beamer-multigraphics/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-beamer-multigraphics.svg?logo=Python&logoColor=white)](https://pypi.org/project/pandoc-beamer-multigraphics/)
[![Pandoc version](https://img.shields.io/badge/pandoc-2.11%20..%203.6-blue.svg?logo=markdown)](https://pandoc.org/)
[![Latest release](https://img.shields.io/github/release-date/chdemko/pandoc-beamer-multigraphics.svg?logo=github)](https://github.com/chdemko/pandoc-beamer-multigraphics/releases)
[![Last commit](https://img.shields.io/github/last-commit/chdemko/pandoc-beamer-multigraphics/develop?logo=github)](https://github.com/chdemko/pandoc-beamer-multigraphics/commit/develop/)
[![Repo Size](https://img.shields.io/github/repo-size/chdemko/pandoc-beamer-multigraphics.svg?logo=github)](http://pandoc-beamer-multigraphics.readthedocs.io/en/latest/)
[![Code Size](https://img.shields.io/github/languages/code-size/chdemko/pandoc-beamer-multigraphics.svg?logo=github)](http://pandoc-beamer-multigraphics.readthedocs.io/en/latest/)
[![Source Rank](https://img.shields.io/librariesio/sourcerank/pypi/pandoc-beamer-multigraphics.svg?logo=libraries.io&logoColor=white)](https://libraries.io/pypi/pandoc-beamer-multigraphics)
[![Docs](https://img.shields.io/readthedocs/pandoc-beamer-multigraphics.svg?logo=read-the-docs&logoColor=white)](http://pandoc-beamer-multigraphics.readthedocs.io/en/latest/)

*pandoc-beamer-multigraphics* is a [pandoc] filter for adding beamer ability
to use multi-images.

[pandoc]: http://pandoc.org/

Instructions
------------

*pandoc-beamer-multigraphics* requires [python], a programming language that
comes pre-installed on linux and Mac OS X, and which is easily installed
[on Windows].

Install *pandoc-beamer-multigraphics* using the bash command

~~~shell-session
$ pipx install pandoc-beamer-multigraphics
~~~

To upgrade to the most recent release, use

~~~shell-session
$ pipx upgrade pandoc-beamer-multigraphics
~~~

`pipx` is a script to install and run python applications in isolated environments from the Python Package Index, [PyPI]. It can be installed using instructions given [here](https://pipx.pypa.io/stable/).

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with pandoc-beamer-multigraphics, please feel
welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-beamer-multigraphics/issues

Contribute
==========

Instructions
------------

Install `hatch`, then run

~~~shell-session
$ hatch run pip install pre-commit
$ hatch run pre-commit install
~~~

to install `pre-commit` before working on your changes.

Tests
-----

When your changes are ready, run

~~~shell-session
$ hatch test
$ hatch fmt --check
$ hatch run lint:check
$ hatch run docs:build
$ hatch build -t wheel
~~~

for running the tests, checking the style, building the documentation
and building the wheel.

