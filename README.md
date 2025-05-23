# trece

[![PyPI](https://img.shields.io/pypi/v/trece.svg)](https://pypi.org/project/trece/)
[![Latest Release](https://img.shields.io/github/v/release/ernestofgonzalez/trece)](https://github.com/ernestofgonzalez/trece/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/ernestofgonzalez/trece/blob/main/LICENSE)


A CLI tool for downloading and managing [CartoCiudad](https://www.cartociudad.es/) data.

CartoCiudad is a comprehensive geospatial database maintained by the [Instituto Geográfico Nacional](https://www.ign.es/). It provides authoritative, up-to-date geographic information for all Spanish provinces, including:

- Administrative boundaries (provinces, municipalities, districts, etc.)
- Road networks and street maps
- Postal codes and census sections
- Points of interest and urban features

CartoCiudad data is widely used for mapping, spatial analysis, urban planning, and research. The data is open, regularly updated, and available in various formats suitable for GIS and data science workflows.


## Features

- **Fast & Simple**: Download CartoCiudad data for all Spanish provinces with a single command.
- **Province Selection**: Choose a province or fetch all at once.
- **Scriptable**: Easily integrate into your data pipelines or automation scripts.


## Getting Started

### Installation

Install via [PyPI](https://pypi.org/)

```bash
pip install trece
```


## Quick Usage

Download CartoCiudad data for all provinces

```bash
trece download
```

or for a single province

```bash
trece download --province Madrid
```


## Command Line Reference

```
trece [OPTIONS] COMMAND [ARGS]...
```

### Commands

- `download` — Download CartoCiudad data

### Options

- `-v, --version` — Print trece version
- `-h, --help` — Show help message and exit
- `-p, --province` — (For `download`) Specify a Spanish province (optional)


## Development

Clone the repository and install development dependencies:

```bash
git clone https://github.com/ernestofgonzalez/trece.git
cd trece
pip install -r requirements.txt
```

Run tests:

```bash
make test
```


## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/ernestofgonzalez/trece/issues) or submit a pull request.


## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.