from dopy.manager import DoError, DoManager


class DoMissingVariableError(DoError):
    def __init__(self, message=None):
        self.message = message
        if message is None:
            self.message = "Missing Required Variable"
        super(DoMissingVariableError, self).__init__(self.message)


class DoEnvironmentError(DoError):
    def __init__(self, message=None):
        self.message = message
        if message is None:
            self.message = """Could not find values for DigitalOcean environment. Required for v2: DO_API_TOKEN. Required for v1: DO_CLIENT_ID, DO_API_KEY"""
        super(DoEnvironmentError, self).__init__(self.message)


class DigitalOceanConnection(object):

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
            'show_droplet': self.manager.show_droplet}

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

    def get_images(self, options=None):
        if options is None:
            options = {'filter': None}
        return self.manager.all_images(**options)
