import click
from do_cli.contexts import CTX
from do_cli.commands.common import host_commands


@click.command('host')
@click.option('-f', '--force-refresh', is_flag=True, help='Pull data from the API')
@click.option('-h', '--host-names', help='Comma separated list of host names')
@CTX
def cli(ctx, force_refresh, host_names):
    """
    Get all Ansible inventory variables about a specific Droplet
    """
    if ctx.verbose:
        click.echo("Get all Ansible inventory variables about a specific Droplet")

    click.echo(host_commands(ctx, force_refresh, host_names))

    if ctx.verbose:
        click.echo('---- cmd_host done ----')
