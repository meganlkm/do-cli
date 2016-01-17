import os

ENV_PREFIX = 'DO_'

#================================================
#   Directory Structure
#================================================
THIS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.getenv('{}BASE_DIR'.format(ENV_PREFIX), THIS_DIR)
PKG_DIR = os.path.join(THIS_DIR, 'do_cli')

#================================================
#   Caching
#================================================
REDIS_CONNINFO = {
    'host': os.getenv('{}REDIS_HOST'.format(ENV_PREFIX), 'localhost'),
    'port': os.getenv('{}REDIS_PORT'.format(ENV_PREFIX), '6379'),
    'db': os.getenv('{}REDIS_DB'.format(ENV_PREFIX), '0')
}
