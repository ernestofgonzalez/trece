import zipfile

import geopandas as gpd
import pytest
from shapely.geometry import Point


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


@pytest.fixture
def real_test_data(tmp_path):
	"""Create a test directory with real GeoPackage data."""
	# Create test data
	points = [Point(0, 0), Point(1, 1), Point(2, 2)]
	data = {'id': [1, 2, 3], 'name': ['Point A', 'Point B', 'Point C'], 'geometry': points}
	gdf = gpd.GeoDataFrame(data, crs='EPSG:4326')

	# Save as GeoPackage
	data_dir = tmp_path / 'test_data'
	data_dir.mkdir()
	gpkg_path = data_dir / 'points.gpkg'
	gdf.to_file(gpkg_path, driver='GPKG')

	# Create multiple zip files with different content
	# Valid zip with GeoPackage
	zip_path_1 = tmp_path / 'valid_data.zip'
	with zipfile.ZipFile(zip_path_1, 'w') as zf:
		zf.write(gpkg_path, gpkg_path.name)

	# Empty zip file
	zip_path_2 = tmp_path / 'empty.zip'
	with zipfile.ZipFile(zip_path_2, 'w'):
		pass

	# Zip with non-GeoPackage content
	zip_path_3 = tmp_path / 'invalid_data.zip'
	dummy_file = data_dir / 'dummy.txt'
	dummy_file.write_text('Not a GeoPackage')
	with zipfile.ZipFile(zip_path_3, 'w') as zf:
		zf.write(dummy_file, dummy_file.name)

	return tmp_path
