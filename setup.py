from setuptools import setup
import os

VERSION = "0.1.0"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="trece",
    description="",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Ernesto González",
    url="https://github.com/ernestofgonzalez/trece",
    project_urls={
        "Issues": "https://github.com/ernestofgonzalez/trece/issues",
        "CI": "https://github.com/ernestofgonzalez/trece/actions",
        "Changelog": "https://github.com/ernestofgonzalez/trece/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["trece"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)