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


Inspecting exampleproject package
---------------------------------

Note: All values are casted to str before printing.

```json
{
    "subpackage": {
        "useless": {
            "funcs": {
                "mul": {
                    "doc": "Multiplies a by b.", 
                    "obj": "<function mul at 0x10c7058c0>", 
                    "params": "(['a', 'b'], [], None, None)"
                }
            }, 
            "doc": "This module contains absolutely useless functions.", 
            "classes": {}, 
            "obj": "<module 'useless' from '/Users/kimmo/code/github/monday/exampleproject/subpackage/useless.pyc'>", 
            "vars": {
                "module_global": {
                    "obj": "this is not used in the module, whatever."
                }
            }
        }
    }, 
    "example": {
        "funcs": {
            "add": {
                "doc": "Returns sum of a, b and c.", 
                "obj": "<function add at 0x10c705848>", 
                "params": "(['a', 'b'], [('c', 0)], None, None)"
            }
        }, 
        "doc": "This is example Python file.", 
        "classes": {
            "Printer": {
                "bases": "(<type 'object'>,)", 
                "obj": "<class 'example.Printer'>", 
                "methods": {
                    "print_text": {
                        "doc": "Prints printer's name and text to stdout.", 
                        "obj": "<unbound method Printer.print_text>", 
                        "params": "(['text'], [], None, None)"
                    }
                }, 
                "vars": {
                    "printer_name": {
                        "obj": "Printer A"
                    }
                }
            }
        }, 
        "obj": "<module 'example' from '/Users/kimmo/code/github/monday/exampleproject/example.pyc'>", 
        "vars": {
            "CONSTANT": {
                "obj": "10"
            }
        }
    }
}
```
