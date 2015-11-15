import click
from do_cli.contexts import CTX
from do_cli.commands.common import host_commands


@click.command('list')
@click.option('-f', '--force-refresh', is_flag=True, help='Pull data from the API')
@CTX
def cli(ctx, force_refresh):
    """
    List all active Droplets as Ansible inventory (default: True)
    """
    if ctx.verbose:
        click.echo("List all active Droplets as Ansible inventory (default: True)")

    click.echo(host_commands(ctx, force_refresh, None))

    if ctx.verbose:
        click.echo('---- cmd_list done ----')
