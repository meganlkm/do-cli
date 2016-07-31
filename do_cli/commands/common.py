import click
from do_cli.cache import DO_CACHE
from do_cli.utils.helpers import str2list
from do_cli.utils.json_helpers import byteify
from do_cli.formatters import format_json


def format_response(data, pretty):
    return format_json(byteify(data)) if pretty else byteify(data)


def get_objects(name, cache_max_age, do_connection, verbose=False):
    objs = DO_CACHE.get_obj(name)
    if objs is None:
        if verbose:
            click.echo("Pulling {} from API".format(name))
        objs = do_connection.do_stuff(name)
        DO_CACHE.set_obj(name, objs, cache_max_age)
    return byteify(objs)


def get_hosts(droplets, host_names):
    host_info = dict()
    for droplet in droplets:
        host_info[droplet["name"]] = {
            "id": droplet["id"],
            "size_slug": droplet["size_slug"],
            "memory": droplet["memory"],
            "disk": droplet["disk"],
            "image_slug": droplet["image"]["slug"],
            "public": droplet["image"]["public"],
            "region_slug": droplet["region"]["slug"],
            "region_name": droplet["region"]["name"],
            "ip_address": droplet["ip_address"]
        }

    if len(host_names):
        host_info = dict((k, v) for k, v in host_info.iteritems() if k in host_names)
    return host_info


def host_commands(ctx, force_refresh, host_names):
    host_names = str2list(host_names, ',')
    if ctx.verbose:
        click.echo(format_response({'host_names': host_names}, True))

    if force_refresh:
        if ctx.verbose:
            click.echo("Forcing refresh of droplets cache")

        ctx.cache.delete('droplets')

    objs = get_objects('droplets', ctx.cache_max_age, ctx.do_conn, ctx.verbose)
    objs = get_hosts(objs, host_names)
    return format_response(objs, ctx.pretty)
