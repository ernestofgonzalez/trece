import asyncio
import logging
from pathlib import Path
from typing import Dict, Optional, Union

from playwright.async_api import Locator, Page, async_playwright

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Downloader:
	"""Downloads CartoCiudad data for Spanish provinces."""

	CARTOCIUDAD_URL = 'https://centrodedescargas.cnig.es/CentroDescargas/cartociudad'

	PROVINCES: Dict[str, str] = {
		'a_coruna': 'A Coruña',
		'albacete': 'Albacete',
		'alicante': 'Alicante/Alacant',
		'almeria': 'Almería',
		'araba': 'Araba/Álava',
		'asturias': 'Asturias',
		'avila': 'Ávila',
		'badajoz': 'Badajoz',
		'baleares': 'Balears, Illes',
		'barcelona': 'Barcelona',
		'bizkaia': 'Bizkaia',
		'burgos': 'Burgos',
		'caceres': 'Cáceres',
		'cadiz': 'Cádiz',
		'cantabria': 'Cantabria',
		'castellon': 'Castellón/Castelló',
		'ceuta': 'Ceuta',
		'ciudad_real': 'Ciudad Real',
		'cordoba': 'Córdoba',
		'cuenca': 'Cuenca',
		'gipuzkoa': 'Gipuzkoa',
		'girona': 'Girona',
		'granada': 'Granada',
		'guadalajara': 'Guadalajara',
		'huelva': 'Huelva',
		'huesca': 'Huesca',
		'jaen': 'Jaén',
		'la_rioja': 'La Rioja',
		'las_palmas': 'Las Palmas',
		'leon': 'León',
		'lleida': 'Lleida',
		'lugo': 'Lugo',
		'madrid': 'Madrid',
		'malaga': 'Málaga',
		'melilla': 'Melilla',
		'murcia': 'Murcia',
		'navarra': 'Navarra',
		'ourense': 'Ourense',
		'palencia': 'Palencia',
		'pontevedra': 'Pontevedra',
		'salamanca': 'Salamanca',
		'santa_cruz_tenerife': 'Santa Cruz de Tenerife',
		'segovia': 'Segovia',
		'san_sebastian': 'San Sebastián',
		'sevilla': 'Sevilla',
		'soria': 'Soria',
		'tarragona': 'Tarragona',
		'teruel': 'Teruel',
		'toledo': 'Toledo',
		'valencia': 'Valencia/València',
		'valladolid': 'Valladolid',
		'zamora': 'Zamora',
		'zaragoza': 'Zaragoza',
	}

	def __init__(self, data_dir: Union[str, Path] = './data'):
		self.data_dir = Path(data_dir)
		self.data_dir.mkdir(exist_ok=True)

	async def _wait_for_table(self, page: Page) -> None:
		"""Wait for table to load"""
		logger.info('Waiting for table to load...')
		await page.wait_for_selector('th.txtTablasCab:has-text("Nombre")', timeout=30000)
		logger.info('Table loaded successfully')

	async def _pagination_ul(self, page: Page) -> Optional[Locator]:
		return await page.query_selector("ul.pagination")

	async def _table_curr_page_nr(self, page: Page) -> Optional[int]:
		pagination_ul = await self._pagination_ul(page)
		if not pagination_ul:
			return None
		
		curr_page_li = await pagination_ul.query_selector("li.page-link.active")
		if not curr_page_li:
			return None
		
		anchor = await curr_page_li.query_selector("a")
		if not anchor:
			return None
		
		anchor_text = await anchor.text_content()
		if not anchor_text:
			return None
			
		try:
			return int(anchor_text.strip())
		except ValueError:
			return None

	async def _load_table_prev_page(self, page: Page) -> None:
		pass

	async def _load_table_next_page(self, page: Page) -> None:
		pass

	async def _query_province_row(self, page: Page, province: str) -> Optional[Locator]:
		"""Find the table row for a specific province."""
		province_name = self.PROVINCES[province]

		logger.info(f'Searching for province row: {province_name}')

		trows = await page.query_selector_all('tr')

		for row in trows:
			name_cell = await row.query_selector('td[data-th="Nombre"] div.col-m-8')
			if name_cell:
				name_text = await name_cell.text_content()
				if province_name.lower() in name_text.lower():
					logger.info(f'Found row for province: {province_name}')
					return row
		logger.warning(f'No row found for province: {province_name}')
		return None

	async def _query_province_download_button(self, page: Page, province: str) -> Optional[Locator]:
		"""Find the download button for a specific province."""
		logger.info(f'Looking for download button for province: {province}')
		row = await self._query_province_row(page, province)
		if not row:
			logger.warning(f'Could not find download button for province: {province}')
			return None

		button = await row.query_selector('a[id^="linkDescDir_"]')
		if button:
			logger.info(f'Found download button for province: {province}')
		else:
			logger.warning(f'Download button not found for province: {province}')
		return button

	async def _download_province(self, page: Page, province: str) -> bool:
		"""Download data for a specific province."""
		logger.info(f'Starting download for province: {province}')
		download_button = await self._query_province_download_button(page, province)
		pass

	async def download(self, province_key: Optional[str] = None) -> None:
		"""
		Download CartoCiudad data for specified province or all provinces.

		Args:
			province_key: Optional specific province to download. If None, downloads all.
		"""
		if province_key:
			logger.info(f'Starting download for specific province: {province_key}')
		else:
			logger.info('Starting download for all provinces')

		provinces_to_download = (
			{province_key: self.PROVINCES[province_key]} if province_key else self.PROVINCES
		)

		async with async_playwright() as p:
			logger.info('Launching browser...')
			browser = await p.chromium.launch(headless=False)
			context = await browser.new_context(
				accept_downloads=True, viewport={'width': 1280, 'height': 800}
			)
			logger.info('Browser launched successfully')

			page = await context.new_page()

			try:
				logger.info(f'Navigating to {self.CARTOCIUDAD_URL}')
				await page.goto(self.CARTOCIUDAD_URL, wait_until='load')
				await self._wait_for_table(page)

				await self._download_province(page, 'a_coruna')

				# for key, name in provinces_to_download.items():
				# 	await self._download_province(key, name, page)
				# 	await asyncio.sleep(2)

			finally:
				logger.info('Closing browser')
				await browser.close()
