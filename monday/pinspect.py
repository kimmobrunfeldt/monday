"""
Project inspect, gathers all modules from a python package.
"""

import os
import sys

import monday.utils


python_extensions = ['.py']
exclude_modules = ['__init__']
respect_init = False
include_import_errors = False


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


def inputdir(path):
    """Returns the absolute path from path which was passed as a
    commandline argument.
    """
    abspath = os.path.abspath(os.path.join(os.getcwd(), path))
    return abspath


def importpath(path):
    """Imports Python module from path and returns the module."""
    moduledir, filename = os.path.split(path)
    modulename, ext = os.path.splitext(filename)

    sys.path.insert(0, moduledir)
    module = __import__(modulename)
    sys.path.remove(moduledir)
    return module


def moduletree(dirpath, python_extensions=python_extensions,
               exclude_modules=exclude_modules, respect_init=respect_init,
               include_import_errors=include_import_errors):
    """Return tree structure of dirpath directorys Python modules."""
    dirpath = inputdir(dirpath)
    tree = utils.defaulttree()

    for directory, dirnames, filenames in os.walk(dirpath):

        if not os.path.isfile(os.path.join(directory, '__init__.py')):
            if respect_init:
                continue

        relativepath = directory[len(dirpath):]
        dircomponents = dirsplit(relativepath)

        for filename in filenames:
            filepath = os.path.abspath(os.path.join(directory, filename))
            head, ext = os.path.splitext(filename)

            if ext in python_extensions and head not in exclude_modules:

                add_module = True
                try:
                    print filepath
                    module = importpath(filepath)
                except ImportError, e:
                    module = e
                    if not include_import_errors:
                        add_module = False

                if add_module:
                    utils.addnode(tree, dircomponents, head, str(module))
    return tree
