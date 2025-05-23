# trece

[![PyPI](https://img.shields.io/pypi/v/trece.svg)](https://pypi.org/project/trece/)
[![Latest Release](https://img.shields.io/github/v/release/ernestofgonzalez/trece)](https://github.com/ernestofgonzalez/trece/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/ernestofgonzalez/trece/blob/main/LICENSE)


A CLI tool for downloading and managing [CartoCiudad](https://www.cartociudad.es/) data.

CartoCiudad is a comprehensive geospatial database maintained by the [Instituto Geográfico Nacional](https://www.ign.es/). It provides authoritative, up-to-date geographic information for all Spanish provinces, including

- Administrative boundaries (provinces, municipalities, districts, etc.)
- Road networks and street maps
- Postal codes and census sections
- Points of interest and urban features

CartoCiudad data is widely used for mapping, spatial analysis, urban planning, and research. The data is open, regularly updated, and available in various formats suitable for GIS and data science workflows.

Each province's dataset is distributed as a GeoPackage (`.gpkg`) file, a spatial database format that supports multiple vector layers. It includes two main layers

- **portalpk_publi**: Point layer representing address portals (building entrances) and kilometer markers along the road network. Each record contains
  - `id`: Unique identifier
  - `geom`: Point geometry (location)
  - `id_porpk`: Portal or kilometer marker ID
  - `tipo_vial`: Type of road/street
  - `nombre_via`: Street name
  - `numero`: Street number or kilometer
  - `extension`: Additional address info
  - `dgc_via`: Road code (from Dirección General de Catastro)
  - `id_pob`: Population entity ID
  - `poblacion`: Population entity name
  - `cod_postal`: Postal code
  - `tipo_porpk`: Portal/marker type
  - `tipoporpkd`: Portal/marker type description
  - `fuented`: Data source
  - `fecha_modificacion`: Last modification date
  - `municipio`: Municipality name
  - `ine_mun`: Municipality code (INE)
  - `provincia`: Province name
  - `comunidad_autonoma`: Autonomous community name

- **manzana**: Polygon layer representing cadastral blocks (manzanas) as defined by the Spanish Cadastre and regional authorities. Each record contains
  - `id`: Unique identifier
  - `geom`: Polygon geometry (block shape)
  - `ID_MANZ`: Block identifier
  - `ALTA_DB`: Database registration date
  - `INE_MUN`: Municipality code (INE)

**Coordinate Reference System:**
- Mainland Spain and Balearic Islands: ETRS89 (EPSG:4258)
- Canary Islands: REGCAN95 (EPSG:4081)

All attributes are standardized for integration with GIS and spatial analysis tools. The data structure and schema are consistent across provinces, enabling automated processing and analysis.


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
trece download --province madrid
```

This will download a ZIP archive for the Madrid province at `./data/CARTOCIUDAD_CALLEJERO_MADRID.zip` by default, but you can specify an output directory with the `-o` option. See the [Options](#options) section for more.


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
- `-o, --output` — (For `download`) Output directory for downloaded files (optional)


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


## Data Source and Attribution

This project uses data from [CartoCiudad](https://www.cartociudad.es/), a product of the [Instituto Geográfico Nacional (IGN)](https://www.ign.es/) and [Centro Nacional de Información Geográfica (CNIG)](https://www.cnig.es/), Spain. For more information, visit: [CartoCiudad](https://www.cartociudad.es/) and [SCNE Productos](https://www.scne.es/productos.php#CartoCiudad).

Attribution:
Fuente: CartoCiudad. © [Instituto Geográfico Nacional de España](https://www.ign.es/), [Centro Nacional de Información Geográfica](https://www.cnig.es/)

Please review the full terms of use and attribution requirements at [https://www.scne.es/productos.php#CartoCiudad](https://www.scne.es/productos.php#CartoCiudad)


## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.