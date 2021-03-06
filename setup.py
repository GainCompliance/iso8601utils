# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pygain-iso8601utils",
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version_format="{tag}",
    setup_requires=["setuptools-git-version==1.0.3"],
    description="Utilities for parsing ISO 8601 times, dates, datetimes, intervals, and durations",
    entry_points={"console_scripts": ["semantic-release = semantic_release.cli:main"]},
    long_description=long_description,
    # The project's main homepage.
    url="https://github.com/silverfernsys/iso8601utils",
    # Author details
    author="Silver Fern Systems",
    author_email="dev@silverfern.io",
    # Choose your license
    license="BSD",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: BSD License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    # What does your project relate to?
    keywords="iso8601 time date datetime duration interval",
    packages=find_packages(),
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=["monthdelta==1.0b", "enum34; python_version < '3.4'"],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        "tests": [
            "pygain-dev~=0.0.1",
            "pytest>=4.4.1,<5.3.0",
            "pytest-cov>=2.7.1,<2.9.0",
            "coverage==5.2.0",
            "flake8~=3.7.1",
            "python-semantic-release==6.4.0; python_version >= '3.7'",
        ]
    },
)
