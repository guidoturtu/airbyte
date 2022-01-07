#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#

import pathlib

from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="octavia-cli",
    version="0.1.0",
    description="A command line interface to manage Airbyte configurations",
    long_description=README,
    author="Airbyte",
    author_email="contact@airbyte.io",
    license="MIT",
    url="https://github.com/airbytehq/airbyte",
    classifiers=[
        # This information is used when browsing on PyPi.
        # Dev Status
        "Development Status :: 3 - Alpha",
        # Project Audience
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        # Python Version Support
        "Programming Language :: Python :: 3.10",
    ],
    keywords="airbyte cli command-line-interface configuration",
    project_urls={
        "Documentation": "https://docs.airbyte.io/",
        "Source": "https://github.com/airbytehq/airbyte",
        "Tracker": "https://github.com/airbytehq/airbyte/issues",
    },
    packages=find_packages(exclude=("tests", "docs")),
    install_requires=["click~=8.0.3"],
    python_requires=">=3.8.12",
    extras_require={
        "dev": ["MyPy~=0.812", "pytest~=6.2.5", "pytest-cov", "pytest-mock", "requests-mock", "pre-commit"],
        "sphinx-docs": [
            "Sphinx~=4.2",
            "sphinx-rtd-theme~=1.0",
        ],
    },
    entry_points={"console_scripts": ["octavia=octavia_cli.entrypoint:octavia"]},
)
