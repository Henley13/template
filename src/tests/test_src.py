# -*- coding: utf-8 -*-
# Author: Arthur Imbert <arthur.imbert.pro@gmail.com>
# License: BSD 3 clause

"""
Unitary tests.
"""

import pytest
from src.mymodule import myfunction, myfunction_bis, myfunction_ter


@pytest.mark.parametrize("value", [0, 1, 2, 3, 4, 5, 0., 1., 2., 3., 4., 5.])
def test_myfunction(value):
    # get value
    xx = myfunction(value)

    # check value
    if isinstance(value, int):
        assert xx == value * value
    else:
        assert xx is None


@pytest.mark.parametrize("value", [0, 1, 2, 3, 4, 5, 0., 1., 2., 3., 4., 5.])
def test_myfunction_bis(value):
    # get value
    xx = myfunction_bis(value)

    # check value
    if isinstance(value, int):
        assert xx == 2 * value
    else:
        assert xx is None


@pytest.mark.parametrize("value", [0, 1, 2, 3, 4, 5, 0., 1., 2., 3., 4., 5.])
def test_myfunction_ter(value):
    # get value
    xx = myfunction_ter(value)

    # check value
    if isinstance(value, int):
        assert xx == 3 * value
    else:
        assert xx is None
