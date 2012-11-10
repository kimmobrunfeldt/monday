import inspect

# This is global
a = 'var'  # adsgga
# sdaf

def deco(func, k=1):
    def innerfunc(*args, **kwargs):
        a = func(*args, **kwargs)
        return str(a)
    return innerfunc


class A(object):
    pass

class B:
    def test(self, (i, k), a, kw=1, *args, **kwargs):
        return 1


def getparams(func):
    """Get the names and default values of a Python function's arguments.
    A tuple of four things is returned: (args, kwargs, argpack, kwargpack).
    args is a list of the argument names (it may contain nested lists).
    kwargs is a list of keyword arguments, single keyword argument is
    a tuple of two items (name, defaultvalue).
    argpack and kwargpack are the names of the * and ** arguments or None.
    """
    argspec = inspect.getargspec(func)

    defaults = argspec.defaults
    if defaults is None:
        defaults = []

    pivot = len(argspec.args) - len(defaults)
    args = argspec.args[:pivot]
    kwargs = []
    for i, arg in enumerate(argspec.args[pivot:]):
            kwargs.append((arg, defaults[i]))

    return (args, kwargs, argspec.varargs, argspec.keywords)


if __name__ == '__main__':
    print A.__bases__
    print B.__bases__
    a = inspect.getargspec(B.test)

    print getparams(B.test)
    print a
    print a.args
    print a.defaults
    #print inspect.getsourcelines(a)
