import os
import sys
from ConfigParser import SafeConfigParser

import click

from do_cli.settings import get_env, PKG_DIR
from do_cli.utils.helpers import exists

CMD_FOLDER = os.path.join(PKG_DIR, 'commands')


class DigitalOceanContext(SafeConfigParser, object):

    def __init__(self, conffile=None):
        super(DigitalOceanContext, self).__init__(allow_no_value=True)
        self.conffile = None
        self.default_section = 'digital_ocean'
        self.set_ini(conffile)
        self.read_environment()

    def __getattr__(self, name):
        value = self.get(self.default_section, name)
        if value is None and name in self.__dict__.keys():
            value = self.__dict__[name]
        return value

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def set_ini(self, ini_filename):
        if ini_filename and exists(ini_filename):
            self.conffile = ini_filename
            self.read()

    def read(self):
        super(DigitalOceanContext, self).read(self.conffile)

    def read_environment(self):
        for env_var in ['client_id', 'api_key', 'api_token', 'api_version', 'image_id',
                        'ssh_key_id', 'wait_timeout', 'size_id', 'region_id']:
            self.__dict__[env_var] = get_env(env_var)

    def setvar(self, name, value):
        if value is not None:
            self.__setattr__(name, value)

    def get(self, section, option):
        if self.has_option(section, option):
            return super(DigitalOceanContext, self).get(section, option)
        return None

    def all(self):
        return self.__dict__


CTX = click.make_pass_decorator(DigitalOceanContext, ensure=True)


class DigitalOceanCLI(click.MultiCommand):

    cmd_dir = CMD_FOLDER
    cmd_namespace = 'do_cli.commands.cmd_'

    def list_commands(self, ctx):
        """ list the commands found in the commands dir """
        rv = []
        for filename in os.listdir(self.cmd_dir):
            if filename.endswith('.py') and filename.startswith('cmd_'):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        """ import the requested command """
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__(self.cmd_namespace + name, None, None, ['cli'])
        except ImportError:
            return
        return mod.cli
