import click
from do_cli.contexts import CTX
from do_cli.formatters.colors import format_json
from do_cli.utils.helpers import get_env_var


@click.command('env')
@CTX
def cli(ctx):
    """
    Display DigitalOcean environment variables
    """
    envdict = dict()

    for varname in ['api_key', 'client_id', 'api_token', 'ssh_key_id', 'size_id', 'region_id',
                    'image_id', 'wait_timeout', 'redis_host', 'redis_port', 'redis_db']:
        key = 'do_{}'.format(varname)
        envdict[key] = get_env_var(key)
    envdict['ctx'] = ctx.all()
    click.echo(format_json(envdict))

    if ctx.verbose:
        click.echo('---- cmd_env done ----')
