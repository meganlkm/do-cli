import click
from do_cli.contexts import CTX
from do_cli.commands.common import host_commands


@click.command('list')
@click.option('-f', '--force-refresh', is_flag=True, help='Pull data from the API')
@click.option('-h', '--host-names', help='Comma separated list of host names')
@CTX
def cli(ctx, force_refresh, host_names):
    """
    Show minimal data for droplets

    --host-names  -h   Comma separated list of host names
        Show minimal data for specific droplets
    """
    if ctx.verbose:
        click.echo("Show minimal data for droplets")

    click.echo(host_commands(ctx, force_refresh, host_names))

    if ctx.verbose:
        click.echo('---- cmd_list done ----')
