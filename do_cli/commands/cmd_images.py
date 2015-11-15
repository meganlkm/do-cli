import click
from do_cli.contexts import CTX
from do_cli.commands.common import format_response, get_objects


@click.command('images')
@click.option('-f', '--force-refresh', is_flag=True, help='Pull data from the API')
@CTX
def cli(ctx, force_refresh):
    """
    List Images as JSON
    """
    if ctx.verbose:
        click.echo("List Images as JSON")

    if force_refresh:
        ctx.cache.delete('images')

    images = get_objects('images', ctx.cache_max_age, ctx.do_conn, ctx.verbose)
    click.echo(format_response(images, ctx.pretty))

    if ctx.verbose:
        click.echo('---- cmd_images done ----')
