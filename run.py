
import monday.pinspect as pinspect
import monday.utils as utils

import os
import sys
import json


path = utils.inputdir(sys.argv[1])
sys.path.insert(0, path)
parentdir = os.path.abspath(os.path.join(path, os.path.pardir))
sys.path.insert(0, parentdir)

tree = pinspect.moduletree(path, include_import_errors=False)
utils.dictmap(tree, pinspect.moduleinfo)
utils.dictmap(tree, str)
print json.dumps(tree, indent=4)
