#!/usr/bin/python
import monday.pinspect as pinspect
import monday.utils as utils

import os
import sys
import json


def main():
    if len(sys.argv) < 2:
        print('Print information about modules in Python project directory.\n')
        print('Usage: python projectinfo.py projectdirectorypath [pythonpath ... ]')
        print('projectdirectorypath  -  path to the Python project.')
        print('pythonpath            -  optional paths to add to sys.path')
        sys.exit(1)

    path = utils.inputdir(sys.argv[1])
    scriptdir = os.path.split(__file__)[0]
    parentdir = os.path.abspath(os.path.join(scriptdir, os.path.pardir))
    sys.path.insert(0, parentdir)

    for pypath in sys.argv[2:]:
        pypath = os.path.abspath(os.path.join(os.getcwd(), pypath))
        sys.path.insert(0, pypath)

    tree = pinspect.ModuleTree(path, include_import_errors=True).gettree()
    pinspect.expand_moduletree(tree)
    utils.dictmap(tree, str)

    print json.dumps(tree, indent=4)


if __name__ == '__main__':
    main()
