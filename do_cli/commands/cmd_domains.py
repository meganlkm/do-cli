import click
from do_cli.contexts import CTX
from do_cli.commands.common import format_response, get_objects


@click.command('domains')
@click.option('-f', '--force-refresh', is_flag=True, help='Pull data from the API')
@CTX
def cli(ctx, force_refresh):
    """
    List Domains as JSON
    """
    if ctx.verbose:
        click.echo("List Domains as JSON")

    if force_refresh:
        ctx.cache.delete('domains')

    domains = get_objects('domains', ctx.cache_max_age, ctx.client, ctx.verbose)
    click.echo(format_response(domains, ctx.pretty))

    if ctx.verbose:
        click.echo('---- cmd_domains done ----')
