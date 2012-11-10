"""
Project inspect, gathers all modules from a python package.
"""

import os
import inspect
import sys

import monday.utils as utils


python_extensions = ['.py']
ignore_modules = ['__init__']
respect_init = False
include_import_errors = True


def issamesource(objlist):
    if len(objlist) < 2:
        return True

    objfile = inspect.getfile(objlist[0])
    objfile = utils.normalize_extension(objfile, ['.pyc'], '.py')
    for obj in objlist[1:]:
        other_objfile = inspect.getfile(obj)
        other_objfile = utils.normalize_extension(other_objfile, ['.pyc'],
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


def moduletree(dirpath, python_extensions=python_extensions,
               ignore_modules=ignore_modules, respect_init=respect_init,
               include_import_errors=include_import_errors):
    """Return tree structure of dirpath directorys Python modules."""
    tree = {}

    for directory, dirnames, filenames in os.walk(dirpath):

        if not os.path.isfile(os.path.join(directory, '__init__.py')):
            if respect_init:
                continue

        relativepath = directory[len(dirpath):]
        dircomponents = dirsplit(relativepath)

        for filename in filenames:
            filepath = os.path.abspath(os.path.join(directory, filename))
            head, ext = os.path.splitext(filename)

            if ext in python_extensions and head not in ignore_modules:

                add_module = True
                try:
                    module = importpath(filepath)
                except Exception, e:
                    module = e
                    if not include_import_errors:
                        add_module = False

                if add_module:
                    utils.addnode(tree, dircomponents, head, module)
    return tree


def moduleinfo(module):
    """Returns information about module."""
    info = {'class': {}, 'func': {}, 'var': {}}
    pred = lambda x: not inspect.ismodule(x)

    for name, member in inspect.getmembers(module, pred):

        if name.startswith('__'):
            continue

        try:
            if not issamesource([module, member]):
                continue
        except TypeError:
            pass

        if inspect.isclass(member):
            info['class'][name] = member
        elif inspect.isfunction(member):
            info['func'][name] = member
        else:
            if not inspect.isbuiltin(member):
                info['var'][name] = member

    return info


def classinfo(cls):
    pass


if __name__ == '__main__':
    module = importpath('monday/test.py')
    print moduleinfo(module)
