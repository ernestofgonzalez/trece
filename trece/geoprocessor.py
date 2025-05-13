import zipfile
from pathlib import Path
from typing import List, Optional, Union

import geopandas as gpd


class GeoPackageProcessor:
	"""Process zipped GeoPackage files from a data directory."""

	def __init__(self, data_dir: Union[str, Path]):
		"""
		Initialize the processor with a data directory path.

		Args:
		    data_dir: Path to the directory containing zip files
		"""
		self.data_dir = Path(data_dir)
		self.temp_dir = self.data_dir / 'temp'
		self._create_temp_dir()

	def _create_temp_dir(self) -> None:
		"""Create temporary directory for unzipped files if it doesn't exist."""
		self.temp_dir.mkdir(parents=True, exist_ok=True)

	def _cleanup_temp_dir(self) -> None:
		"""Remove all files in temporary directory."""
		if self.temp_dir.exists():
			for item in self.temp_dir.iterdir():
				if item.is_file():
					item.unlink()
				elif item.is_dir():
					for subitem in item.iterdir():
						subitem.unlink()
					item.rmdir()
			self.temp_dir.rmdir()

	def _unzip_file(self, zip_path: Path) -> Path:
		"""
		Unzip a file to the temporary directory.

		Args:
		    zip_path: Path to the zip file

		Returns:
		    Path to the unzipped directory
		"""
		extract_path = self.temp_dir / zip_path.stem
		with zipfile.ZipFile(zip_path, 'r') as zip_ref:
			zip_ref.extractall(extract_path)
		return extract_path

	def _find_gpkg_file(self, directory: Path) -> Optional[Path]:
		"""
		Find the first .gpkg file in a directory.

		Args:
		    directory: Path to search for .gpkg files

		Returns:
		    Path to the first .gpkg file found or None
		"""
		for item in directory.rglob('*.gpkg'):
			return item
		return None

	def process_data(self) -> List[gpd.GeoDataFrame]:
		"""
		Process all zip files in the data directory and read their GeoPackages.

		Returns:
		    List of GeoDataFrames from all processed GeoPackage files
		"""
		geodataframes = []

		try:
			for zip_file in self.data_dir.glob('*.zip'):
				unzipped_dir = self._unzip_file(zip_file)
				gpkg_file = self._find_gpkg_file(unzipped_dir)

				if gpkg_file:
					gdf = gpd.read_file(gpkg_file)
					geodataframes.append(gdf)

		finally:
			self._cleanup_temp_dir()

		return geodataframes
