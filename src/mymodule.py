# -*- coding: utf-8 -*-
# Author: Arthur Imbert <arthur.imbert.pro@gmail.com>
# License: BSD 3 clause

"""Module function."""


def myfunction(x):
    """Return the square of the value."""
    if isinstance(x, int):
        xx = x * x
    else:
        xx = None

    return xx


def myfunction_bis(x):
    """Multiply the value by 2."""
    if isinstance(x, int):
        xx = 2 * x
    else:
        xx = None

    return xx
