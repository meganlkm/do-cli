import os
import click

from do_cli.cache import DO_CACHE
from do_cli.contexts import CTX, DigitalOceanCLI
from do_cli.digitalocean import DigitalOceanConnection
from do_cli.formatters import format_json
from do_cli.settings import BASE_DIR


@click.group(chain=True, cls=DigitalOceanCLI)
@click.option('--cache-path', help='Path to the cache files (default: .)')
@click.option('-a', '--api-key', help='Set the DigitalOcean API Key')
@click.option('-c', '--client-id', help='Set the DigitalOcean Client ID')
@click.option('-m', '--cache-max-age', help='Maximum age of the cached items (default: 0)')
@click.option('-p', '--pretty', is_flag=True, help='Pretty-print results')
@click.option('-v', '--verbose', is_flag=True)
@CTX
def cli(ctx, *args, **kwargs):
    ctx.set_ini(os.path.join(BASE_DIR, 'digital_ocean.ini'))
    for name in ['api_key', 'cache_max_age', 'cache_path', 'client_id', 'pretty', 'verbose']:
        ctx.setvar(name, kwargs[name])
    ctx.cache = DO_CACHE

    do_conn_kwargs = {
        'api_version': ctx.api_version,
        'api_token': ctx.api_token,
        'client_id': ctx.client_id,
        'api_key': ctx.api_key
    }
    ctx.do_conn = DigitalOceanConnection(**do_conn_kwargs)

    if ctx.verbose:
        click.echo(format_json({
            'ctx': ctx.all(),
            'cache_path': ctx.cache_path
        }))
        click.echo('---- cli.cli done ----')


if __name__ == '__main__':
    cli()
