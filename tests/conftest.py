import zipfile

import geopandas as gpd
import pytest


@pytest.fixture
def temp_data_dir(tmp_path):
	"""Create a temporary directory with test data."""
	# Create a test GeoPackage
	gdf = gpd.GeoDataFrame({'id': [1, 2], 'geometry': None})
	gpkg_path = tmp_path / 'test.gpkg'
	gdf.to_file(gpkg_path, driver='GPKG')

	# Create a zip file containing the GeoPackage
	zip_path = tmp_path / 'test_data.zip'
	with zipfile.ZipFile(zip_path, 'w') as zf:
		zf.write(gpkg_path, gpkg_path.name)

	return tmp_path
