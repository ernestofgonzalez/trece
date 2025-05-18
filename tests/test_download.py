import pytest
import pytest_asyncio
from playwright.async_api import Page, async_playwright

from trece.download import Downloader


@pytest_asyncio.fixture
async def browser():
	async with async_playwright() as p:
		browser = await p.chromium.launch()
		yield browser
		await browser.close()


@pytest_asyncio.fixture
async def page(browser):
	page = await browser.new_page()
	yield page
	await page.close()


@pytest_asyncio.fixture
def downloader():
	return Downloader()


@pytest_asyncio.fixture
async def page_with_table(page: Page):
	# Await the page object first
	page = await anext(page) if hasattr(page, '__anext__') else page
	# Load mock table HTML
	await page.set_content("""
        <table class="table table-bordered table-hover tablaAdaptable tablaAdaptableCab">
            <thead>
                <tr><th class="txtTablasCab">Nombre</th></tr>
            </thead>
            <tbody>
                <tr class="fontSize08em row100">
                    <td data-th="Nombre" class="lineHeightTD15">
                        <div class="col-m-3 tablaAdaptableCeldas lineHeight30 displayInlineBlock"><b>Archivo</b></div>
                        <div class="col-m-8 lineHeight30 displayInlineBlock txtLeftCenterTablas">A Coruña</div>
                    </td>
                </tr>
                <tr class="fontSize08em row100">
                    <td data-th="Nombre" class="lineHeightTD15">
                        <div class="col-m-3 tablaAdaptableCeldas lineHeight30 displayInlineBlock"><b>Archivo</b></div>
                        <div class="col-m-8 lineHeight30 displayInlineBlock txtLeftCenterTablas">Barcelona</div>
                    </td>
                </tr>
            </tbody>
        </table>
    """)

	return page


@pytest.mark.asyncio
async def test_table_curr_page_nr(page, downloader):
	pagination_ul = """
		<ul class="pagination floatDer">
			<li class="page-link active"><a class="page-link colorAzulClaro" href="#" title="1">1</a></li>
			<li><a id="linkPag_2" class="page-link colorAzulClaro" href="#" title="2">2</a></li>																			
			<li><a id="linkPag_3" class="page-link colorAzulClaro" href="#" title="3">3</a></li>										
			<li><a id="linkPag_2" class="page-link colorAzulClaro" href="#" aria-label="Siguiente" title="Siguiente"><span aria-hidden="true">»</span></a></li>
			<li><a id="linkPag_3" class="page-link colorAzulClaro" href="#" aria-label="Última" title="Última"><span aria-hidden="true">»»</span></a></li>		 
		</ul>
	"""

	page = await anext(page) if hasattr(page, '__anext__') else page
	await page.set_content(pagination_ul)

	curr_page_nr = await downloader._table_curr_page_nr(page)

	assert curr_page_nr == 1


@pytest.mark.asyncio
async def test_query_existing_province(page_with_table, downloader):
	row = await downloader._query_province_row(page_with_table, 'barcelona')
	assert row is not None
	text = await row.text_content()
	assert 'Barcelona' in text


@pytest.mark.asyncio
async def test_query_case_insensitive(page_with_table, downloader):
	row = await downloader._query_province_row(page_with_table, 'a_coruna')
	assert row is not None
	text = await row.text_content()
	assert 'A Coruña' in text


@pytest.mark.asyncio
async def test_query_nonexistent_province(page_with_table, downloader):
	row = await downloader._query_province_row(page_with_table, 'madrid')
	assert row is None


@pytest.mark.asyncio
async def test_query_invalid_province(page_with_table, downloader):
	with pytest.raises(KeyError):
		await downloader._query_province_row(page_with_table, 'invalid_province')


@pytest.mark.asyncio
async def test_query_empty_table(page: Page, downloader):
	await page.set_content('<table><tbody></tbody></table>')
	row = await downloader._query_province_row(page, 'barcelona')
	assert row is None
