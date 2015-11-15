import os


def get_env_var(key):
    return os.getenv(key.upper(), None)


def exists(src):
    """ alias for os.path.exists """
    return os.path.exists(src)


def remove(src):
    """ alias for os.remove """
    return os.remove(src)


def push(my_dict, key, element):
    """ Push an element into an array that may not have been defined in the dict """
    if key not in my_dict.keys():
        my_dict[key] = list()
    my_dict[key].append(element)
    return my_dict


def str2list(value, delimiter):
    return [] if value is None else value.split(delimiter)


def get_cell_width(data):
    return len(max([i for i in data], key=len))


def pretty_table(data):
    """ data is a string delimited by whitespace """
    data = data.split('\n')
    widths = [get_cell_width(row) for row in list(zip(*[line.split() for line in data]))]
    data = list([line.split() for line in data])

    tr_border = '+-{}-+'.format('-+-'.join(['-' * w for w in widths]))
    formatter = '|' + ''.join([' {:^%s} |' % w for w in widths])

    table = [tr_border]
    for col in data:
        table.append(formatter.format(*col))

    table.insert(2, tr_border)
    table.append(tr_border)

    return '\n'.join(table)
