# trece

[![PyPI](https://img.shields.io/pypi/v/trece.svg)](https://pypi.org/project/trece/)
[![Latest Release](https://img.shields.io/github/v/release/ernestofgonzalez/trece)](https://github.com/ernestofgonzalez/trece/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/ernestofgonzalez/trece/blob/main/LICENSE)

A Python CLI tool for downloading and managing CartoCiudad data for Spanish provinces.

## Features

- Programatic download of [CartoCiudad data for Spanish provinces](https://centrodedescargas.cnig.es/CentroDescargas/cartociudad)

## Installation

Install trece using pip:

```bash
pip install trece
```

## Usage

trece provides a command-line interface

```bash
trece [OPTIONS] COMMAND [ARGS]...
```

### Commands 

- `download` - Download CartoCiudad data

### Options

  - `-v, --version` - Print trece version.
  - `-h, --help` - Show this message and exit.

## Development

To contribute to trece, first clone the repository:

```bash
git clone https://github.com/ernestofgonzalez/trece.git
cd trece
```

Install development dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
make test
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
