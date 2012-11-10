"""
General functions etc.
"""

import os


def addnode(tree, nodepath, newkey, value):
    """Adds a node to nodepath's end.
    Note: Modifies tree in place.
    """
    if not len(nodepath):
        tree[newkey] = value
        return

    node = tree
    for key in nodepath:
        if key not in node:
            node[key] = {}
        node = node[key]

    node[newkey] = value


def dictmap(dictionary, func):
    """Calls a function for all non-dictionary values in an arbitrary deeply
    nested dictionary.
    Note: Remember recursion depth limit.
    Note: Dictionary is modified in place.

    Args:
        dicionary: What dictionary to travel.
        func: Function to call for each value.
    """
    for key, value in dictionary.iteritems():
        if isinstance(value, dict):
            dictmap(value, func)
        else:
            dictionary[key] = func(value)


def inputdir(path):
    """Returns the absolute path from path which was passed as a
    commandline argument.
    """
    abspath = os.path.abspath(os.path.join(os.getcwd(), path))
    return abspath


def normalize_extension(path, possible_extensions, default_extension):
    head, ext = os.path.splitext(path)
    if not ext:
        return path

    if ext in possible_extensions:
        ext = default_extension
    return head + ext
