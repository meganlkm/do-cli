import click
from do_cli.contexts import CTX


@click.command('flush-cache')
@CTX
def cli(ctx):
    """
    clear the cache
    """
    if ctx.verbose:
        click.echo("clear the cache")

    ctx.cache.flushdb()

    if ctx.verbose:
        click.echo('---- cmd_flush-cache done ----')
