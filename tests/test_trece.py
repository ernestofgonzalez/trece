import geopandas as gpd

from trece import GeoPackageProcessor


def test_geopackage_processor(temp_data_dir):
	processor = GeoPackageProcessor(temp_data_dir)
	results = processor.process_data()

	assert len(results) == 1
	assert isinstance(results[0], gpd.GeoDataFrame)
	assert len(results[0]) == 2


def test_geopackage_processor_with_real_data(real_test_data):
	processor = GeoPackageProcessor(real_test_data)
	results = processor.process_data()

	# Should only process the valid GeoPackage
	assert len(results) == 1

	# Verify the content of the GeoDataFrame
	gdf = results[0]
	assert isinstance(gdf, gpd.GeoDataFrame)
	assert len(gdf) == 3
	assert all(col in gdf.columns for col in ['id', 'name', 'geometry'])
	assert gdf.crs.to_string() == 'EPSG:4326'


def test_geopackage_processor_empty_directory(tmp_path):
	processor = GeoPackageProcessor(tmp_path)
	results = processor.process_data()
	assert len(results) == 0


def test_geopackage_processor_cleanup(real_test_data):
	processor = GeoPackageProcessor(real_test_data)
	temp_dir = processor.temp_dir

	# Process data and verify cleanup
	processor.process_data()
	assert not temp_dir.exists()
