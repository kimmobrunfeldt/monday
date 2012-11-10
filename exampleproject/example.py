"""This is example Python file."""


CONSTANT = 10


def add(a, b, c=0):
    """Returns sum of a, b and c."""

    return a + b + c


class Printer(object):
    """Provides printing capabilities."""
    printer_name = 'Printer A'

    def print_text(self, text):
        """Prints printer's name and text to stdout."""
        print(self.printer_name)
        print(text)
