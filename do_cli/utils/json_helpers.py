from json import dumps
from datetime import datetime


def json_serial(obj):
    """ JSON serializer for objects not serializable by default json code """
    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial


def pretty_print(obj, sort_keys=True, indent=4, separators=(',', ': ')):
    """ return nicely formatted json """
    return dumps(obj, sort_keys=sort_keys, indent=indent,
                 separators=separators, default=json_serial)


def byteify(data, is_deep=False):
    if isinstance(data, unicode):
        return data.encode('utf-8')
    if isinstance(data, list):
        return [byteify(item, True) for item in data]
    if isinstance(data, dict) and not is_deep:
        return {byteify(key, True): byteify(value, True) for key, value in data.iteritems()}
    return data
