import click

from do_cli.contexts import CTX
from do_cli.formatters import format_json
from do_cli.settings import get_env

DO_VARS = [
    'api_key', 'client_id', 'api_token', 'ssh_key_id', 'size_id', 'region_id',
    'image_id', 'wait_timeout', 'redis_host', 'redis_port', 'redis_db'
]


@click.command('env')
@CTX
def cli(ctx):
    """
    Display DigitalOcean environment variables
    """
    envdict = dict()

    for varname in DO_VARS:
        envdict['do_{}'.format(varname)] = get_env(varname)

    envdict['ctx'] = ctx.all()
    click.echo(format_json(envdict))

    if ctx.verbose:
        click.echo('---- cmd_env done ----')
