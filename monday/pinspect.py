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


class ModuleTree(object):
    """Provides useful operations for a directory which contains Python
    modules.

    Args:
        dirpath: Path of the directory to inspect.
    """
    def __init__(self, dirpath, python_extensions=python_extensions,
                 ignore_modules=ignore_modules, respect_init=respect_init,
                 include_import_errors=include_import_errors):
        self.dirpath = dirpath

        self.python_extensions = python_extensions
        self.ignore_modules = ignore_modules
        self.respect_init = respect_init
        self.include_import_errors = include_import_errors

        self._createtree()

    def gettree(self):
        """Returns module tree."""
        return self._tree

    def _createtree(self):
        """Creates the tree of modules."""
        self._tree = {}
        for directory, dirnames, filenames in os.walk(self.dirpath):

            if not os.path.isfile(os.path.join(directory, '__init__.py')):
                if self.respect_init:
                    continue

            for filename in filenames:
                self._createnode(directory, filename)

    def _createnode(self, directory, filename):
        """Creates single node(module) to the tree of modules."""
        relativepath = directory[len(self.dirpath):]
        dircomponents = utils.dirsplit(relativepath)

        filepath = os.path.abspath(os.path.join(directory, filename))
        head, ext = os.path.splitext(filename)

        if ext in self.python_extensions and head not in self.ignore_modules:
            add_module = True
            try:
                module = utils.importpath(filepath)
            except Exception, e:
                module = e
                if not self.include_import_errors:
                    add_module = False

            if add_module:
                utils.addnode(self._tree, dircomponents, head, module)


def getdoc(obj):
    return inspect.getdoc(obj)


def moduleinfo(module, expand=False):
    """Returns classes, functions and module level variables of a module.
    """
    info = {'doc': getdoc(module), 'obj': module,
            'classes': {}, 'funcs': {}, 'vars': {}}
    pred = lambda x: not inspect.ismodule(x)

    for name, member in inspect.getmembers(module, pred):

        if name.startswith('__'):
            continue

        try:
            if not utils.issamesource([module, member]):
                continue
        except TypeError:
            pass

        if inspect.isclass(member):
            info['classes'][name] = classinfo(member)
        elif inspect.isfunction(member):
            info['funcs'][name] = funcinfo(member)
        else:
            if not inspect.isbuiltin(member):
                info['vars'][name] = varinfo(member)

    return info


def classinfo(cls):
    """Return information about class cls in dict format."""
    info = {'obj': cls, 'bases': cls.__bases__, 'methods': {}, 'vars': {}}

    for name, member in inspect.getmembers(cls):

        if name.startswith('__'):
            continue

        try:
            if not utils.issamesource([cls, member]):
                continue
        except TypeError:
            pass

        if inspect.ismethod(member):
            info['methods'][name] = methodinfo(member)
        else:
            if not inspect.isbuiltin(member):
                info['vars'][name] = memberinfo(member)
    return info


def getparams(func, ismethod=False):
    """Get the names and default values of a Python function's arguments.
    A tuple of four things is returned: (args, kwargs, argpack, kwargpack).
    args is a list of the argument names (it may contain nested lists).
    kwargs is a list of keyword arguments, single keyword argument is
    a tuple of two items (name, defaultvalue).
    argpack and kwargpack are the names of the * and ** arguments or None.
    If ismethod is True, first argument of args is removed.
    """
    argspec = inspect.getargspec(func)

    defaults = argspec.defaults
    if defaults is None:
        defaults = []

    pivot = len(argspec.args) - len(defaults)
    args = argspec.args[:pivot]
    if ismethod:
        args.pop(0)

    kwargs = []
    for i, arg in enumerate(argspec.args[pivot:]):
            kwargs.append((arg, defaults[i]))

    return (args, kwargs, argspec.varargs, argspec.keywords)


def memberinfo(var):
    return {'obj': var}


def methodinfo(method):
    params = getparams(method, ismethod=True)
    return {'doc': getdoc(method), 'obj': method, 'params': params}


def funcinfo(func):
    params = getparams(func)
    return {'doc': getdoc(func), 'obj': func, 'params': params}


def varinfo(var):
    return {'obj': var}


def expand_moduletree(moduletree):
    """Expands moduletree so it will contain all information in its branches.
    Note: moduletree is modified in-place.
    """
    # For all non-dict values, call moduleinfo.
    expanded_moduleinfo = lambda x: moduleinfo(x, expand=True)
    utils.dictmap(moduletree, expanded_moduleinfo)
