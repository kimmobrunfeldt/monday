"""
General functions etc.
"""

import copy
import os
import sys
import inspect


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


def dictmap(dictionary, func, copy=False):
    """Calls a function for all non-dictionary values in an arbitrary deeply
    nested dictionary.
    Note: Remember recursion depth limit.
    Note: Dictionary is modified in place.

    Args:
        dicionary: What dictionary to travel.
        func: Function to call for each value.
    Kwargs:
        copy: If True, original dictionary won't be modified.
    """
    def inner_dictmap(dictionary, func):
        for key, value in dictionary.iteritems():
            if isinstance(value, dict):
                dictmap(value, func)
            else:
                dictionary[key] = func(value)

    if copy:
        new_dictionary = copy.deepcopy(dictionary)
    else:
        new_dictionary = dictionary

    inner_dictmap(new_dictionary, func)
    return new_dictionary


def importpath(path):
    """Imports Python module from path and returns the module."""
    moduledir, filename = os.path.split(path)
    modulename, ext = os.path.splitext(filename)

    sys.path.insert(0, moduledir)
    try:
        module = __import__(modulename)
    except SystemExit:
        return ImportError('File \'%s\' raised SystemExit.' % path)
    sys.path.remove(moduledir)
    sys.stdout = sys.__stdout__
    return module


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


def issamesource(objlist):
    """Takes a list of objects and returns True if they all have the same
    source file. Source filenames are normalized, so file.py and file.pyc are
    the same thing.
    """
    if len(objlist) < 2:
        return True

    objfile = inspect.getfile(objlist[0])
    objfile = normalize_extension(objfile, ['.pyc'], '.py')
    for obj in objlist[1:]:
        other_objfile = inspect.getfile(obj)
        other_objfile = normalize_extension(other_objfile, ['.pyc'],
                                            '.py')

        if objfile != other_objfile:
            return False
    return True


def dirsplit(path):
    """Splits path to its directory components.
    '/home/xx'' -> ['home', 'xx']
    '/home/xx' -> ['home', 'xx']
    """
    components = []
    if not len(path):
        return components

    path = path.strip('\\/')

    component = True
    while component:
        path, component = os.path.split(path)
        if len(component):
            components.append(component)

    components.reverse()
    return components
