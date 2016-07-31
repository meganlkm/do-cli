import fnmatch

from dopy.manager import DoManager
from do_cli.exceptions import DoEnvironmentError


class DigitalOceanClient(object):

    def __init__(self, api_version=None, api_token=None, client_id=None, api_key=None):
        self.api_version = int(api_version)
        self.api_token = api_token
        self.client_id = client_id
        self.api_key = api_key
        self.validate_config()
        self.manager = self.get_do_manager()

        self.method_map = {
            'regions': self.manager.all_regions,
            'images': self.get_images,
            'sizes': self.manager.sizes,
            'ssh_keys': self.manager.all_ssh_keys,
            'domains': self.manager.all_domains,
            'droplets': self.manager.all_active_droplets,
            'destroy_droplet': self.manager.destroy_droplet,
            'create_droplet': self.manager.new_droplet,
            'show_droplet': self.manager.show_droplet
        }

    def validate_config(self):
        if self.api_version == 2:
            return self.validate_v2_config()
        elif self.api_version == 1:
            return self.validate_v1_config()
        raise DoEnvironmentError()

    def validate_v1_config(self):
        if not all([self.api_key, self.client_id]):
            raise DoEnvironmentError("v1 config failed. Required for v1: DO_CLIENT_ID, DO_API_KEY")
        return True

    def validate_v2_config(self):
        if self.api_token in [None, '']:
            raise DoEnvironmentError("v2 config failed. Required for v2: DO_API_TOKEN")
        return True

    def get_do_manager(self):
        if self.api_version == 2:
            return DoManager(None, self.api_token, api_version=2)
        return DoManager(self.client_id, self.api_key, api_version=self.api_version)

    def do_stuff(self, name, params=None):
        if params:
            return self.method_map[name](**params)
        return self.method_map[name]()

    def get_images(self, filter_opts=dict()):
        images = self.manager.all_images()
        if len(filter_opts):
            tmp_images = []
            for img in images:
                tmp = []
                for key, value in filter_opts.iteritems():
                    if isinstance(value, bool):
                        if img[key] is value:
                            tmp.append(img)
                    elif isinstance(value, list):
                        if set(value).issubset(img[key]):
                            tmp.append(img)
                    elif value is None or any([isinstance(value, int), isinstance(value, float)]):
                        if value == img[key]:
                            tmp.append(img)
                    else:
                        try:
                            if fnmatch.fnmatch(img[key], value):
                                tmp.append(img)
                        except:
                            if img[key] == value:
                                tmp.append(img)
                if len(tmp) == len(filter_opts.keys()):
                    tmp_images.append(img)
            images = tmp_images
        return {'images': images, 'count': len(images)}
