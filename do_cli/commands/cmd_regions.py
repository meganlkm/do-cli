import click
from do_cli.contexts import CTX
from do_cli.commands.common import format_response, get_objects


@click.command('regions')
@click.option('-f', '--force-refresh', is_flag=True, help='Pull data from the API')
@CTX
def cli(ctx, force_refresh):
    """
    List Regions as JSON
    """
    if ctx.verbose:
        click.echo("List Regions as JSON")

    if force_refresh:
        ctx.cache.delete('regions')

    regions = get_objects('regions', ctx.cache_max_age, ctx.client, ctx.verbose)
    click.echo(format_response(regions, ctx.pretty))

    if ctx.verbose:
        click.echo('---- cmd_regions done ----')
