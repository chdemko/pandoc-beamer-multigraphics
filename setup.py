"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/chdemko/pandoc-beamer-multigraphics
"""

# To use a consistent encoding
from os import path

# Always prefer setuptools over distutils
from setuptools import setup

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "README.md"), encoding="utf-8") as stream:
    LONG_DESCRIPTION = stream.read()

setup(
    name="pandoc-beamer-multigraphics",
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version="0.1.0",
    # The project's description
    description="A pandoc filter for adding beamer multigraphics ability",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    # The project's main homepage.
    url="https://github.com/chdemko/pandoc-beamer-multigraphics",
    # The project's download page
    download_url="https://github.com/chdemko/pandoc-beamer-multigraphics/archive/master.zip",
    # Author details
    author="Christophe Demko",
    author_email="chdemko@gmail.com",
    # Maintainer details
    maintainer="Christophe Demko",
    maintainer_email="chdemko@gmail.com",
    # Choose your license
    license="BSD-3-Clause",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Specify the OS
        "Operating System :: OS Independent",
        # Indicate who your project is intended for
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Documentation",
        "Topic :: Text Processing :: Filters",
        # Specify the Python versions you support HERE. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3.6",
        # Natural language used
        "Natural Language :: English",
    ],
    # What does your project relate to?
    keywords="pandoc, filters, graphics, latex, beamer",
    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    py_modules=["pandoc_beamer_multigraphics"],
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        "console_scripts": [
            "pandoc-beamer-multigraphics = pandoc_beamer_multigraphics:main"
        ]
    },
    # List run-time dependencies HERE.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=["panflute>=1.12"],
    # List additional groups of dependencies HERE (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        "dev": ["check-manifest"],
        "docs": [
            "sphinx>=3.2",
            "sphinx_rtd_theme>=0.5",
        ],
        "test": ["pytest-cov", "black", "doc8", "pylint>=2.6", "panflute>=1.12"],
    },
    # If there are data files included in your packages that need to be
    # installed, specify them HERE.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={},
)