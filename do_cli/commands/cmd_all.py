import click
from do_cli.contexts import CTX
from do_cli.commands.common import format_response, get_objects


@click.command('all')
@click.option('-f', '--force-refresh', is_flag=True, help='Pull data from the API')
@CTX
def cli(ctx, force_refresh):
    """
    List all DigitalOcean information as JSON
    """
    if ctx.verbose:
        click.echo("List all DigitalOcean information as JSON")

    data = dict()
    for obj in ['regions', 'images', 'sizes', 'ssh_keys', 'domains', 'droplets']:
        if force_refresh:
            ctx.cache.delete(obj)
        data[obj] = get_objects(obj, ctx.cache_max_age, ctx.do_conn, ctx.verbose)
    click.echo(format_response(data, ctx.pretty))

    if ctx.verbose:
        click.echo('---- cmd_all done ----')
