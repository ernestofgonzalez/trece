# trece

[![PyPI](https://img.shields.io/pypi/v/trece.svg)](https://pypi.org/project/trece/)
[![Latest Release](https://img.shields.io/github/v/release/ernestofgonzalez/trece)](https://github.com/ernestofgonzalez/trece/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/ernestofgonzalez/trece/blob/main/LICENSE)


A CLI tool for downloading and managing [CartoCiudad](https://centrodedescargas.cnig.es/CentroDescargas/cartociudad) data for all Spanish provinces.


## Features

- **Fast & Simple**: Download CartoCiudad data for all Spanish provinces with a single command.
- **Province Selection**: Choose a province or fetch all at once.
- **Scriptable**: Easily integrate into your data pipelines or automation scripts.


## Getting Started

### Installation

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