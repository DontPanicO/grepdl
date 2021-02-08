#!/usr/bin/python3

import setuptools

long_description = """A command line interface to grep
live text streams of docker logs.
"""

setuptools.setup(
    name="grepdl",
    version="1.0",
    author="Andrea Tedeschi",
    author_email="andrea.tedeschi@andreatedeschi.uno",
    description="Grep docker logs",
    long_description=long_description,
    long_description_content_type="text",
    license="Apache 2.0",
    url="https://git.metodogroup.it/andrea.tedeschi/grepdl",
    python_requires=">=3.6",
    platforms='posix',
    scripts=["bin/grepdl"],
)

