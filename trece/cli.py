import asyncio

import click

from trece.download import Downloader

VERSION = '0.0.0a1'


def print_version(ctx, param, value):
	if not value or ctx.resilient_parsing:
		return
	click.echo(VERSION)
	ctx.exit()


@click.group(
	context_settings=dict(help_option_names=['-h', '--help']),
)
@click.option(
	'-v',
	'--version',
	is_flag=True,
	callback=print_version,
	expose_value=False,
	is_eager=True,
	help='Print trece version.',
)
@click.pass_context
def main(ctx):
	ctx.ensure_object(dict)


@main.command()
@click.option(
	'-p',
	'--province',
	required=False,
)
@click.option(
	'-o',
	'--output',
	required=False,
	type=click.Path(file_okay=False, dir_okay=True, writable=True, resolve_path=True),
	help='Output directory for downloaded files.',
)
@click.pass_context
def download(ctx, province, output):
	"""Download CartoCiudad data."""
	downloader = Downloader(data_dir=output) if output else Downloader()
	asyncio.run(downloader.download(province))
