""" redis utils for the do_cli """

# pylint: disable=star-args
# pylint: disable=too-many-public-methods

import pickle
from redis import StrictRedis
from do_cli.settings import REDIS_CONNINFO


class DOCache(StrictRedis):

    """
    along with everything from StrictRedis,
    provide functionality to easily cache complex objects.
    """

    def __init__(self):
        super(DOCache, self).__init__(**REDIS_CONNINFO)

    def set_obj(self, key, value_obj, expires=0):
        """ pickle value_obj and cache it """
        if expires:
            self.setex(key, expires, pickle.dumps(value_obj))
            return
        self.set(key, pickle.dumps(value_obj))

    def get_obj(self, key):
        """ get the pickled object from cache and load it """
        obj = self.get(key)
        try:
            obj = pickle.loads(obj)
        except TypeError:
            obj = None
        return obj


DO_CACHE = DOCache()
