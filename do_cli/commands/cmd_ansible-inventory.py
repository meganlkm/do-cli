import click
from do_cli.contexts import CTX
from do_cli.commands.common import format_response, get_objects
from do_cli.utils.helpers import push
from do_cli.utils.json_helpers import byteify


@click.command('ansible-inventory')
@click.option('-f', '--force-refresh', is_flag=True, help='Pull data from the API')
@CTX
def cli(ctx, force_refresh):
    """
    Generate Ansible inventory
    """
    if ctx.verbose:
        click.echo("Generate Ansible inventory")

    if force_refresh:
        ctx.cache.delete('inventory')
        ctx.cache.delete('droplets')

    inventory = ctx.cache.get_obj('inventory')
    droplets = {}
    if inventory is None:
        inventory = {}
        droplets = get_objects('droplets', ctx.cache_max_age, ctx.do_conn, ctx.verbose)

        for droplet in droplets:
            dest = droplet['ip_address']

            inventory[droplet['id']] = [dest]
            inventory = push(inventory, droplet['name'], dest)
            inventory = push(inventory, 'region_{}'.format(droplet['region']['slug']), dest)

            components = droplet['name'].split('.')
            if len(components) == 3:
                inventory = push(inventory, components[0], dest)
                inventory = push(inventory, "{}_{}".format(components[0], components[1]), dest)

    inventory = byteify(inventory)
    ctx.cache.set_obj('inventory', inventory, ctx.cache_max_age)
    click.echo(format_response(inventory, ctx.pretty))

    if ctx.verbose:
        click.echo('---- cmd_ansible-inventory done ----')
