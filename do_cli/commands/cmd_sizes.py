import click
from do_cli.contexts import CTX
from do_cli.commands.common import format_response, get_objects


@click.command('sizes')
@click.option('-f', '--force-refresh', is_flag=True, help='Pull data from the API')
@CTX
def cli(ctx, force_refresh):
    """
    List Sizes as JSON
    """
    if ctx.verbose:
        click.echo("List Sizes as JSON")

    if force_refresh:
        ctx.cache.delete('sizes')

    sizes = get_objects('sizes', ctx.cache_max_age, ctx.do_conn, ctx.verbose)
    click.echo(format_response(sizes, ctx.pretty))

    if ctx.verbose:
        click.echo('---- cmd_sizes done ----')
