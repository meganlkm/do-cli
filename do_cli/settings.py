import os

ENV_PREFIX = 'DO_'


def get_env(var_name, default=None):
    return os.getenv('{}{}'.format(ENV_PREFIX, var_name.upper()), default)


#================================================
#   Directory Structure
#================================================
THIS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = get_env('BASE_DIR', THIS_DIR)
PKG_DIR = os.path.join(THIS_DIR, 'do_cli')

#================================================
#   Caching
#================================================
REDIS_CONNINFO = {
    'host': get_env('REDIS_HOST', 'localhost'),
    'port': get_env('REDIS_PORT', '6379'),
    'db': get_env('REDIS_DB', '0')
}
