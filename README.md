Monday – *Gathers documentation for you.*
=========================================

![LOGO](https://github.com/kimmobrunfeldt/monday/raw/master/img/mondaysmall.png)

Monday is automatic documentation generator for Python.

**This is a work in progress!**
*projectinfo.py* is currently working but outputs a raw JSON.
Also, decorators, properties and many other Python features are not inspected correctly.

projectinfo.py
--------------

    Print information about modules in Python project directory.
    
    Usage: python projectinfo.py projectdirectorypath [pythonpath ... ]
    projectdirectorypath  -  path to the Python project.
    pythonpath            -  optional paths to add to sys.path


Output of monday package
------------------------

    {
        "utils": {
            "funcs": {
                "addnode": {
                    "doc": "Adds a node to nodepath's end.\nNote: Modifies tree in place.", 
                    "obj": "<function addnode at 0x1048246e0>", 
                    "params": "(['tree', 'nodepath', 'newkey', 'value'], [], None, None)"
                }, 
                "normalize_extension": {
                    "doc": "None", 
                    "obj": "<function normalize_extension at 0x1048248c0>", 
                    "params": "(['path', 'possible_extensions', 'default_extension'], [], None, None)"
                }, 
                "importpath": {
                    "doc": "Imports Python module from path and returns the module.", 
                    "obj": "<function importpath at 0x1048247d0>", 
                    "params": "(['path'], [], None, None)"
                }, 
                "inputdir": {
                    "doc": "Returns the absolute path from path which was passed as a\ncommandline argument.", 
                    "obj": "<function inputdir at 0x104824848>", 
                    "params": "(['path'], [], None, None)"
                }, 
                "issamesource": {
                    "doc": "Takes a list of objects and returns True if they all have the same\nsource file. Source filenames are normalized, so file.py and file.pyc are\nthe same thing.", 
                    "obj": "<function issamesource at 0x104824938>", 
                    "params": "(['objlist'], [], None, None)"
                }, 
                "dirsplit": {
                    "doc": "Splits path to its directory components.\n'/home/xx'' -> ['home', 'xx']\n'/home/xx' -> ['home', 'xx']", 
                    "obj": "<function dirsplit at 0x1048249b0>", 
                    "params": "(['path'], [], None, None)"
                }, 
                "dictmap": {
                    "doc": "Calls a function for all non-dictionary values in an arbitrary deeply\nnested dictionary.\nNote: Remember recursion depth limit.\nNote: Dictionary is modified in place.\n\nArgs:\n    dicionary: What dictionary to travel.\n    func: Function to call for each value.\nKwargs:\n    copy: If True, original dictionary won't be modified.", 
                    "obj": "<function dictmap at 0x104824758>", 
                    "params": "(['dictionary', 'func'], [('copy', False)], None, None)"
                }
            }, 
            "doc": "General functions etc.", 
            "classes": {}, 
            "obj": "<module 'utils' from '/Users/kimmo/code/github/monday/monday/utils.pyc'>", 
            "vars": {}
        }, 
        "docopt": {
            "funcs": {
                "parse_argv": {
                    "doc": "None", 
                    "obj": "<function parse_argv at 0x10481fc80>", 
                    "params": "(['source', 'options'], [], None, None)"
                }, 
                "parse_long": {
                    "doc": "None", 
                    "obj": "<function parse_long at 0x104815b90>", 
                    "params": "(['tokens', 'options'], [], None, None)"
                }, 
                "parse_pattern": {
                    "doc": "None", 
                    "obj": "<function parse_pattern at 0x10481faa0>", 
                    "params": "(['source', 'options'], [], None, None)"
                }, 
                "parse_expr": {
                    "doc": "expr ::= seq ( '|' seq )* ;", 
                    "obj": "<function parse_expr at 0x10481fb18>", 
                    "params": "(['tokens', 'options'], [], None, None)"
                }, 
                "parse_seq": {
                    "doc": "seq ::= ( atom [ '...' ] )* ;", 
                    "obj": "<function parse_seq at 0x10481fb90>", 
                    "params": "(['tokens', 'options'], [], None, None)"
                }, 
                "parse_doc_options": {
                    "doc": "None", 
                    "obj": "<function parse_doc_options at 0x10481fcf8>", 
                    "params": "(['doc'], [], None, None)"
                }, 
                "formal_usage": {
                    "doc": "None", 
                    "obj": "<function formal_usage at 0x10481fde8>", 
                    "params": "(['printable_usage'], [], None, None)"
                }, 
                "parse_shorts": {
                    "doc": "None", 
                    "obj": "<function parse_shorts at 0x10481fa28>", 
                    "params": "(['tokens', 'options'], [], None, None)"
                }, 
                "extras": {
                    "doc": "None", 
                    "obj": "<function extras at 0x10481fe60>", 
                    "params": "(['help', 'version', 'options', 'doc'], [], None, None)"
                }, 
                "printable_usage": {
                    "doc": "None", 
                    "obj": "<function printable_usage at 0x10481fd70>", 
                    "params": "(['doc'], [], None, None)"
                }, 
                "parse_atom": {
                    "doc": "atom ::= '(' expr ')' | '[' expr ']' | 'options'\n| long | shorts | argument | command ;", 
                    "obj": "<function parse_atom at 0x10481fc08>", 
                    "params": "(['tokens', 'options'], [], None, None)"
                }, 
                "docopt": {
                    "doc": "None", 
                    "obj": "<function docopt at 0x10481fed8>", 
                    "params": "(['doc'], [('argv', ['monday']), ('help', True), ('version', None)], None, None)"
                }
            }, 
            "doc": "None", 
            "classes": {
                "ParrentPattern": {
                    "bases": "(<class 'docopt.Pattern'>,)", 
                    "obj": "<class 'docopt.ParrentPattern'>", 
                    "methods": {
                        "fix": {
                            "doc": "None", 
                            "obj": "<unbound method ParrentPattern.fix>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_list_arguments": {
                            "doc": "Find arguments that should accumulate values and fix them.", 
                            "obj": "<unbound method ParrentPattern.fix_list_arguments>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_identities": {
                            "doc": "Make pattern-tree tips point to same object if they are equal.", 
                            "obj": "<unbound method ParrentPattern.fix_identities>", 
                            "params": "([], [('uniq', None)], None, None)"
                        }
                    }, 
                    "vars": {
                        "flat": {
                            "obj": "<property object at 0x10481d940>"
                        }, 
                        "either": {
                            "obj": "<property object at 0x10481d7e0>"
                        }
                    }
                }, 
                "TokenStream": {
                    "bases": "(<type 'list'>,)", 
                    "obj": "<class 'docopt.TokenStream'>", 
                    "methods": {
                        "current": {
                            "doc": "None", 
                            "obj": "<unbound method TokenStream.current>", 
                            "params": "([], [], None, None)"
                        }, 
                        "move": {
                            "doc": "None", 
                            "obj": "<unbound method TokenStream.move>", 
                            "params": "([], [], None, None)"
                        }
                    }, 
                    "vars": {
                        "count": {
                            "obj": "<method 'count' of 'list' objects>"
                        }, 
                        "index": {
                            "obj": "<method 'index' of 'list' objects>"
                        }, 
                        "reverse": {
                            "obj": "<method 'reverse' of 'list' objects>"
                        }, 
                        "extend": {
                            "obj": "<method 'extend' of 'list' objects>"
                        }, 
                        "insert": {
                            "obj": "<method 'insert' of 'list' objects>"
                        }, 
                        "pop": {
                            "obj": "<method 'pop' of 'list' objects>"
                        }, 
                        "sort": {
                            "obj": "<method 'sort' of 'list' objects>"
                        }, 
                        "remove": {
                            "obj": "<method 'remove' of 'list' objects>"
                        }, 
                        "append": {
                            "obj": "<method 'append' of 'list' objects>"
                        }
                    }
                }, 
                "Option": {
                    "bases": "(<class 'docopt.ChildPattern'>,)", 
                    "obj": "<class 'docopt.Option'>", 
                    "methods": {
                        "fix_list_arguments": {
                            "doc": "Find arguments that should accumulate values and fix them.", 
                            "obj": "<unbound method Option.fix_list_arguments>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_identities": {
                            "doc": "Make pattern-tree tips point to same object if they are equal.", 
                            "obj": "<unbound method Option.fix_identities>", 
                            "params": "([], [('uniq', None)], None, None)"
                        }, 
                        "fix": {
                            "doc": "None", 
                            "obj": "<unbound method Option.fix>", 
                            "params": "([], [], None, None)"
                        }, 
                        "parse": {
                            "doc": "None", 
                            "obj": "<bound method type.parse of <class 'docopt.Option'>>", 
                            "params": "(['option_description'], [], None, None)"
                        }, 
                        "single_match": {
                            "doc": "None", 
                            "obj": "<unbound method Option.single_match>", 
                            "params": "(['left'], [], None, None)"
                        }, 
                        "match": {
                            "doc": "None", 
                            "obj": "<unbound method Option.match>", 
                            "params": "(['left'], [('collected', None)], None, None)"
                        }
                    }, 
                    "vars": {
                        "flat": {
                            "obj": "<property object at 0x10481d890>"
                        }, 
                        "either": {
                            "obj": "<property object at 0x10481d7e0>"
                        }, 
                        "name": {
                            "obj": "<property object at 0x10481db50>"
                        }
                    }
                }, 
                "Pattern": {
                    "bases": "(<type 'object'>,)", 
                    "obj": "<class 'docopt.Pattern'>", 
                    "methods": {
                        "fix": {
                            "doc": "None", 
                            "obj": "<unbound method Pattern.fix>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_list_arguments": {
                            "doc": "Find arguments that should accumulate values and fix them.", 
                            "obj": "<unbound method Pattern.fix_list_arguments>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_identities": {
                            "doc": "Make pattern-tree tips point to same object if they are equal.", 
                            "obj": "<unbound method Pattern.fix_identities>", 
                            "params": "([], [('uniq', None)], None, None)"
                        }
                    }, 
                    "vars": {
                        "either": {
                            "obj": "<property object at 0x10481d7e0>"
                        }
                    }
                }, 
                "Required": {
                    "bases": "(<class 'docopt.ParrentPattern'>,)", 
                    "obj": "<class 'docopt.Required'>", 
                    "methods": {
                        "fix": {
                            "doc": "None", 
                            "obj": "<unbound method Required.fix>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_list_arguments": {
                            "doc": "Find arguments that should accumulate values and fix them.", 
                            "obj": "<unbound method Required.fix_list_arguments>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_identities": {
                            "doc": "Make pattern-tree tips point to same object if they are equal.", 
                            "obj": "<unbound method Required.fix_identities>", 
                            "params": "([], [('uniq', None)], None, None)"
                        }, 
                        "match": {
                            "doc": "None", 
                            "obj": "<unbound method Required.match>", 
                            "params": "(['left'], [('collected', None)], None, None)"
                        }
                    }, 
                    "vars": {
                        "flat": {
                            "obj": "<property object at 0x10481d940>"
                        }, 
                        "either": {
                            "obj": "<property object at 0x10481d7e0>"
                        }
                    }
                }, 
                "DocoptLanguageError": {
                    "bases": "(<type 'exceptions.Exception'>,)", 
                    "obj": "<class 'docopt.DocoptLanguageError'>", 
                    "methods": {}, 
                    "vars": {
                        "message": {
                            "obj": "<attribute 'message' of 'exceptions.BaseException' objects>"
                        }, 
                        "args": {
                            "obj": "<attribute 'args' of 'exceptions.BaseException' objects>"
                        }
                    }
                }, 
                "Argument": {
                    "bases": "(<class 'docopt.ChildPattern'>,)", 
                    "obj": "<class 'docopt.Argument'>", 
                    "methods": {
                        "fix": {
                            "doc": "None", 
                            "obj": "<unbound method Argument.fix>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_list_arguments": {
                            "doc": "Find arguments that should accumulate values and fix them.", 
                            "obj": "<unbound method Argument.fix_list_arguments>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_identities": {
                            "doc": "Make pattern-tree tips point to same object if they are equal.", 
                            "obj": "<unbound method Argument.fix_identities>", 
                            "params": "([], [('uniq', None)], None, None)"
                        }, 
                        "single_match": {
                            "doc": "None", 
                            "obj": "<unbound method Argument.single_match>", 
                            "params": "(['left'], [], None, None)"
                        }, 
                        "match": {
                            "doc": "None", 
                            "obj": "<unbound method Argument.match>", 
                            "params": "(['left'], [('collected', None)], None, None)"
                        }
                    }, 
                    "vars": {
                        "flat": {
                            "obj": "<property object at 0x10481d890>"
                        }, 
                        "either": {
                            "obj": "<property object at 0x10481d7e0>"
                        }
                    }
                }, 
                "OneOrMore": {
                    "bases": "(<class 'docopt.ParrentPattern'>,)", 
                    "obj": "<class 'docopt.OneOrMore'>", 
                    "methods": {
                        "fix": {
                            "doc": "None", 
                            "obj": "<unbound method OneOrMore.fix>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_list_arguments": {
                            "doc": "Find arguments that should accumulate values and fix them.", 
                            "obj": "<unbound method OneOrMore.fix_list_arguments>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_identities": {
                            "doc": "Make pattern-tree tips point to same object if they are equal.", 
                            "obj": "<unbound method OneOrMore.fix_identities>", 
                            "params": "([], [('uniq', None)], None, None)"
                        }, 
                        "match": {
                            "doc": "None", 
                            "obj": "<unbound method OneOrMore.match>", 
                            "params": "(['left'], [('collected', None)], None, None)"
                        }
                    }, 
                    "vars": {
                        "flat": {
                            "obj": "<property object at 0x10481d940>"
                        }, 
                        "either": {
                            "obj": "<property object at 0x10481d7e0>"
                        }
                    }
                }, 
                "ChildPattern": {
                    "bases": "(<class 'docopt.Pattern'>,)", 
                    "obj": "<class 'docopt.ChildPattern'>", 
                    "methods": {
                        "fix": {
                            "doc": "None", 
                            "obj": "<unbound method ChildPattern.fix>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_list_arguments": {
                            "doc": "Find arguments that should accumulate values and fix them.", 
                            "obj": "<unbound method ChildPattern.fix_list_arguments>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_identities": {
                            "doc": "Make pattern-tree tips point to same object if they are equal.", 
                            "obj": "<unbound method ChildPattern.fix_identities>", 
                            "params": "([], [('uniq', None)], None, None)"
                        }, 
                        "match": {
                            "doc": "None", 
                            "obj": "<unbound method ChildPattern.match>", 
                            "params": "(['left'], [('collected', None)], None, None)"
                        }
                    }, 
                    "vars": {
                        "flat": {
                            "obj": "<property object at 0x10481d890>"
                        }, 
                        "either": {
                            "obj": "<property object at 0x10481d7e0>"
                        }
                    }
                }, 
                "Dict": {
                    "bases": "(<type 'dict'>,)", 
                    "obj": "<class 'docopt.Dict'>", 
                    "methods": {}, 
                    "vars": {
                        "viewitems": {
                            "obj": "<method 'viewitems' of 'dict' objects>"
                        }, 
                        "setdefault": {
                            "obj": "<method 'setdefault' of 'dict' objects>"
                        }, 
                        "get": {
                            "obj": "<method 'get' of 'dict' objects>"
                        }, 
                        "keys": {
                            "obj": "<method 'keys' of 'dict' objects>"
                        }, 
                        "items": {
                            "obj": "<method 'items' of 'dict' objects>"
                        }, 
                        "clear": {
                            "obj": "<method 'clear' of 'dict' objects>"
                        }, 
                        "popitem": {
                            "obj": "<method 'popitem' of 'dict' objects>"
                        }, 
                        "update": {
                            "obj": "<method 'update' of 'dict' objects>"
                        }, 
                        "pop": {
                            "obj": "<method 'pop' of 'dict' objects>"
                        }, 
                        "viewkeys": {
                            "obj": "<method 'viewkeys' of 'dict' objects>"
                        }, 
                        "viewvalues": {
                            "obj": "<method 'viewvalues' of 'dict' objects>"
                        }, 
                        "has_key": {
                            "obj": "<method 'has_key' of 'dict' objects>"
                        }, 
                        "values": {
                            "obj": "<method 'values' of 'dict' objects>"
                        }, 
                        "itervalues": {
                            "obj": "<method 'itervalues' of 'dict' objects>"
                        }, 
                        "iteritems": {
                            "obj": "<method 'iteritems' of 'dict' objects>"
                        }, 
                        "copy": {
                            "obj": "<method 'copy' of 'dict' objects>"
                        }, 
                        "iterkeys": {
                            "obj": "<method 'iterkeys' of 'dict' objects>"
                        }
                    }
                }, 
                "Either": {
                    "bases": "(<class 'docopt.ParrentPattern'>,)", 
                    "obj": "<class 'docopt.Either'>", 
                    "methods": {
                        "fix": {
                            "doc": "None", 
                            "obj": "<unbound method Either.fix>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_list_arguments": {
                            "doc": "Find arguments that should accumulate values and fix them.", 
                            "obj": "<unbound method Either.fix_list_arguments>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_identities": {
                            "doc": "Make pattern-tree tips point to same object if they are equal.", 
                            "obj": "<unbound method Either.fix_identities>", 
                            "params": "([], [('uniq', None)], None, None)"
                        }, 
                        "match": {
                            "doc": "None", 
                            "obj": "<unbound method Either.match>", 
                            "params": "(['left'], [('collected', None)], None, None)"
                        }
                    }, 
                    "vars": {
                        "flat": {
                            "obj": "<property object at 0x10481d940>"
                        }, 
                        "either": {
                            "obj": "<property object at 0x10481d7e0>"
                        }
                    }
                }, 
                "DocoptExit": {
                    "bases": "(<type 'exceptions.SystemExit'>,)", 
                    "obj": "<class 'docopt.DocoptExit'>", 
                    "methods": {}, 
                    "vars": {
                        "code": {
                            "obj": "<member 'code' of 'exceptions.SystemExit' objects>"
                        }, 
                        "usage": {
                            "obj": ""
                        }, 
                        "message": {
                            "obj": "<attribute 'message' of 'exceptions.BaseException' objects>"
                        }, 
                        "args": {
                            "obj": "<attribute 'args' of 'exceptions.BaseException' objects>"
                        }
                    }
                }, 
                "Command": {
                    "bases": "(<class 'docopt.Argument'>,)", 
                    "obj": "<class 'docopt.Command'>", 
                    "methods": {
                        "fix": {
                            "doc": "None", 
                            "obj": "<unbound method Command.fix>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_list_arguments": {
                            "doc": "Find arguments that should accumulate values and fix them.", 
                            "obj": "<unbound method Command.fix_list_arguments>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_identities": {
                            "doc": "Make pattern-tree tips point to same object if they are equal.", 
                            "obj": "<unbound method Command.fix_identities>", 
                            "params": "([], [('uniq', None)], None, None)"
                        }, 
                        "single_match": {
                            "doc": "None", 
                            "obj": "<unbound method Command.single_match>", 
                            "params": "(['left'], [], None, None)"
                        }, 
                        "match": {
                            "doc": "None", 
                            "obj": "<unbound method Command.match>", 
                            "params": "(['left'], [('collected', None)], None, None)"
                        }
                    }, 
                    "vars": {
                        "flat": {
                            "obj": "<property object at 0x10481d890>"
                        }, 
                        "either": {
                            "obj": "<property object at 0x10481d7e0>"
                        }
                    }
                }, 
                "Optional": {
                    "bases": "(<class 'docopt.ParrentPattern'>,)", 
                    "obj": "<class 'docopt.Optional'>", 
                    "methods": {
                        "fix": {
                            "doc": "None", 
                            "obj": "<unbound method Optional.fix>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_list_arguments": {
                            "doc": "Find arguments that should accumulate values and fix them.", 
                            "obj": "<unbound method Optional.fix_list_arguments>", 
                            "params": "([], [], None, None)"
                        }, 
                        "fix_identities": {
                            "doc": "Make pattern-tree tips point to same object if they are equal.", 
                            "obj": "<unbound method Optional.fix_identities>", 
                            "params": "([], [('uniq', None)], None, None)"
                        }, 
                        "match": {
                            "doc": "None", 
                            "obj": "<unbound method Optional.match>", 
                            "params": "(['left'], [('collected', None)], None, None)"
                        }
                    }, 
                    "vars": {
                        "flat": {
                            "obj": "<property object at 0x10481d940>"
                        }, 
                        "either": {
                            "obj": "<property object at 0x10481d7e0>"
                        }
                    }
                }
            }, 
            "obj": "<module 'docopt' from '/Users/kimmo/code/github/monday/monday/docopt.pyc'>", 
            "vars": {}
        }, 
        "pinspect": {
            "funcs": {
                "getdoc": {
                    "doc": "None", 
                    "obj": "<function getdoc at 0x1048159b0>", 
                    "params": "(['obj'], [], None, None)"
                }, 
                "memberinfo": {
                    "doc": "None", 
                    "obj": "<function memberinfo at 0x104824398>", 
                    "params": "(['var'], [], None, None)"
                }, 
                "classinfo": {
                    "doc": "Return information about class cls in dict format.", 
                    "obj": "<function classinfo at 0x1048242a8>", 
                    "params": "(['cls'], [], None, None)"
                }, 
                "getparams": {
                    "doc": "Get the names and default values of a Python function's arguments.\nA tuple of four things is returned: (args, kwargs, argpack, kwargpack).\nargs is a list of the argument names (it may contain nested lists).\nkwargs is a list of keyword arguments, single keyword argument is\na tuple of two items (name, defaultvalue).\nargpack and kwargpack are the names of the * and ** arguments or None.\nIf ismethod is True, first argument of args is removed.", 
                    "obj": "<function getparams at 0x104824320>", 
                    "params": "(['func'], [('ismethod', False)], None, None)"
                }, 
                "varinfo": {
                    "doc": "None", 
                    "obj": "<function varinfo at 0x104824500>", 
                    "params": "(['var'], [], None, None)"
                }, 
                "moduleinfo": {
                    "doc": "Returns classes, functions and module level variables of a module.\n    ", 
                    "obj": "<function moduleinfo at 0x104824230>", 
                    "params": "(['module'], [('expand', False)], None, None)"
                }, 
                "methodinfo": {
                    "doc": "None", 
                    "obj": "<function methodinfo at 0x104824410>", 
                    "params": "(['method'], [], None, None)"
                }, 
                "funcinfo": {
                    "doc": "None", 
                    "obj": "<function funcinfo at 0x104824488>", 
                    "params": "(['func'], [], None, None)"
                }, 
                "expand_moduletree": {
                    "doc": "Expands moduletree so it will contain all information in its branches.\nNote: moduletree is modified in-place.", 
                    "obj": "<function expand_moduletree at 0x104824578>", 
                    "params": "(['moduletree'], [], None, None)"
                }
            }, 
            "doc": "Project inspect, gathers all modules from a python package.", 
            "classes": {
                "ModuleTree": {
                    "bases": "(<type 'object'>,)", 
                    "obj": "<class 'pinspect.ModuleTree'>", 
                    "methods": {
                        "_createtree": {
                            "doc": "Creates the tree of modules.", 
                            "obj": "<unbound method ModuleTree._createtree>", 
                            "params": "([], [], None, None)"
                        }, 
                        "gettree": {
                            "doc": "Returns module tree.", 
                            "obj": "<unbound method ModuleTree.gettree>", 
                            "params": "([], [], None, None)"
                        }, 
                        "_createnode": {
                            "doc": "Creates single node(module) to the tree of modules.", 
                            "obj": "<unbound method ModuleTree._createnode>", 
                            "params": "(['directory', 'filename'], [], None, None)"
                        }
                    }, 
                    "vars": {}
                }
            }, 
            "obj": "<module 'pinspect' from '/Users/kimmo/code/github/monday/monday/pinspect.pyc'>", 
            "vars": {
                "python_extensions": {
                    "obj": "['.py']"
                }, 
                "respect_init": {
                    "obj": "False"
                }, 
                "ignore_modules": {
                    "obj": "['__init__']"
                }, 
                "include_import_errors": {
                    "obj": "True"
                }
            }
        }
    }
