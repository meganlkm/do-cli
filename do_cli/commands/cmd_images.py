import click
from do_cli.contexts import CTX
from do_cli.commands.common import format_response


@click.command('images')
@click.option('-f', '--force-refresh', is_flag=True, help='Pull data from the API')
@click.option('--public/--private', default=True, help='This is a boolean value that indicates whether the image in question is public or not. An image that is public is available to all accounts. A non-public image is only accessible from your account.')
@click.option('-m', '--min-disk-size', type=int, help="The minimum 'disk' required for a size to use this image.")
@click.option('-g', '--size-gigabytes', type=float, help="The size of the image in gigabytes.")
@click.option('-s', '--slug', help='A uniquely identifying string that is associated with each of the DigitalOcean-provided public images. These can be used to reference a public image as an alternative to the numeric id.')
@click.option('-n', '--name', help='The display name that has been given to an image. This is what is shown in the control panel and is generally a descriptive title for the image in question.')
@click.option('-i', '--id', help='A unique number that can be used to identify and reference a specific image.')
@click.option('-r', '--regions', help='This attribute is an array of the regions that the image is available in. The regions are represented by their identifying slug values.')
@click.option('-d', '--distribution', help='This attribute describes the base distribution used for this image.')
@click.option('-t', '--type', help='The kind of image, describing the duration of how long the image is stored. This is either "snapshot" or "backup".')
@CTX
def cli(ctx, force_refresh, *args, **kwargs):
    """
    List Images as JSON
    """
    if ctx.verbose:
        click.echo("List Images as JSON")

    if force_refresh:
        ctx.cache.delete('images')

    filter_opts = dict((k, v) for k, v in kwargs.iteritems() if v is not None)
    if 'regions' in filter_opts:
        filter_opts['regions'] = filter_opts['regions'].split(',')
    images = ctx.client.get_images(filter_opts)
    click.echo(format_response(images, ctx.pretty))

    if ctx.verbose:
        click.echo('---- cmd_images done ----')
