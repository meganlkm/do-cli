from datetime import datetime

import click
from do_cli.contexts import CTX
from do_cli.commands.common import format_response, get_objects
from do_cli.exceptions import DoMissingVariableError


def list_all(ctx):
    """
    List Droplets as JSON
    """
    return get_objects('droplets', ctx.cache_max_age, ctx.client, ctx.verbose)


def create(ctx):
    """
    Create a new Droplet
    """
    if ctx.droplet_name is None:
        raise DoMissingVariableError("Missing droplet_name")

    conf = {'name': ctx.droplet_name, 'size_id': ctx.size_id,
            'image_id': ctx.image_id, 'region_id': ctx.region_id,
            'ssh_key_ids': [ctx.ssh_key_id, ]}

    response = ctx.client.do_stuff('create_droplet', conf)
    if ctx.verbose:
        click.echo(response)
        click.echo('---- cmd_droplets:create done -----')
    return response


def destroy(ctx):
    """
    Destroy specific droplet
    """
    if ctx.verbose:
        click.echo("Destroy specific droplet")

    if ctx.droplet_id is None:
        raise DoMissingVariableError("Missing droplet_id")

    if ctx.verbose:
        click.echo("Attempting to destroy droplet_id: {}".format(ctx.droplet_id))

    response = ctx.client.do_stuff('destroy_droplet', {'droplet_id': ctx.droplet_id})
    if ctx.verbose:
        click.echo(response)
        click.echo('---- cmd_droplets:destroy done ----')

    return response


def show(ctx):
    """
    Show specific droplet
    """
    if ctx.verbose:
        click.echo("Show specific droplet")

    if ctx.droplet_id is None:
        raise DoMissingVariableError("Missing droplet_id")

    if ctx.verbose:
        click.echo("Attempting to show droplet_id: {}".format(ctx.droplet_id))

    response = ctx.client.do_stuff('show_droplet', {'droplet_id': ctx.droplet_id})
    if ctx.verbose:
        click.echo(response)
        click.echo('---- cmd_droplets:show done ----')

    return response


def snapshot(ctx):
    if ctx.verbose:
        click.echo("Create a snapshot")

    if ctx.droplet_id is None:
        raise DoMissingVariableError("Missing droplet_id")

    if ctx.name is None:
        ctx.name = datetime.utcnow().strftime('%Y%m%d-%H%M%S')

    params = {'droplet_id': ctx.droplet_id, 'name': ctx.name}
    if ctx.verbose:
        click.echo("Attempting to create snapshot: {}".format(params))

    response = ctx.client.do_stuff('snapshot_droplet', params)
    if ctx.verbose:
        click.echo(response)
        click.echo('---- cmd_droplets:show done ----')

    return response


DROPLET_ACTIONS = {
    'list': list_all,
    'create': create,
    'destroy': destroy,
    'show': show,
    'snapshot': snapshot,
}


@click.command('droplets')
@click.option('-f', '--force-refresh', is_flag=True, help='Pull data from the API')
@click.option('--droplet-id', type=click.INT, help='the id of the droplet to act on')
@click.option('--create', is_flag=True, help='Create a new droplet')
@click.option('--destroy', is_flag=True, help='Destroy a droplet')
@click.option('--show', is_flag=True, help='Show a droplet')
@click.option('--snapshot', is_flag=True, help='Create a snapshot')
@click.option('--name', help='name of a new droplet')
@CTX
def cli(ctx, force_refresh, droplet_id, create, destroy, show, name, snapshot):
    """
    Droplet CRUD
    """
    if ctx.verbose:
        click.echo("Droplet CRUD")

    ctx.droplet_id = droplet_id
    ctx.droplet_name = name

    if force_refresh:
        ctx.cache.delete('droplets')

    action = 'list'
    if create:
        action = 'create'
    elif destroy:
        action = 'destroy'
    elif show:
        action = 'show'
    elif snapshot:
        action = 'snapshot'

    response = DROPLET_ACTIONS[action](ctx)
    click.echo(format_response(response, ctx.pretty))

    if ctx.verbose:
        click.echo('---- cmd_droplets done ----')
