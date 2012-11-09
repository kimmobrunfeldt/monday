"""
General functions etc.
"""

import collections


def defaulttree():
    """https://gist.github.com/2012250"""
    return collections.defaultdict(defaulttree)


def addnode(tree, nodepath, key, value):
    """Adds a node to nodepath's end.
    XXX: .update() 3 times..
    """
    if not len(nodepath):
        tree.update({key: value})
        return

    key = nodepath[0]
    node = tree[key]
    for key in nodepath[1:-1]:
        node = node[key]

    if len(nodepath) > 1:
        node[nodepath[-1]].update({key: value})
    else:
        tree[key].update({key: value})
