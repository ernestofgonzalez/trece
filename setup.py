import os

from setuptools import find_packages, setup

VERSION = '0.0.0a1'


def get_long_description():
	with open(
		os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md'),
		encoding='utf8',
	) as fp:
		return fp.read()


setup(
	name='trece',
	description='A CLI tool for downloading authoritative Spanish geospatial and address data.',
	long_description=get_long_description(),
	long_description_content_type='text/markdown',
	author='Ernesto González',
	url='https://github.com/ernestofgonzalez/trece',
	project_urls={
		'Source code': 'https://github.com/ernestofgonzalez/trece',
		'Issues': 'https://github.com/ernestofgonzalez/trece/issues',
		'CI': 'https://github.com/ernestofgonzalez/trece/actions',
		'Changelog': 'https://github.com/ernestofgonzalez/trece/releases',
	},
	license='Apache License, Version 2.0',
	version=VERSION,
	packages=find_packages(),
	entry_points={
		'console_scripts': [
			'trece = trece.cli:main',
		]
	},
	install_requires=[
		'click',
		'geopandas>=0.12.0',
		'pandas>=1.5.0',
		'playwright',
	],
	extras_require={'test': ['pytest']},
	python_requires='>=3.10',
	classifiers=[
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Libraries',
		'Topic :: Utilities',
		'Programming Language :: Python :: 3.10',
		'Programming Language :: Python :: 3.11',
		'Programming Language :: Python :: 3.12',
		'Programming Language :: Python :: 3.13',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX',
		'Operating System :: Unix',
		'Operating System :: MacOS',
	],
)
