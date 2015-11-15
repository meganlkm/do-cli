import click
from do_cli.contexts import CTX
from do_cli.commands.common import format_response, get_objects


@click.command('ssh-keys')
@click.option('-f', '--force-refresh', is_flag=True, help='Pull data from the API')
@CTX
def cli(ctx, force_refresh):
    """
    List SSH keys as JSON
    """
    if ctx.verbose:
        click.echo("List SSH keys as JSON")

    if force_refresh:
        ctx.cache.delete('ssh_keys')

    ssh_keys = get_objects('ssh_keys', ctx.cache_max_age, ctx.do_conn, ctx.verbose)
    click.echo(format_response(ssh_keys, ctx.pretty))

    if ctx.verbose:
        click.echo('---- cmd_ssh-keys done ----')
