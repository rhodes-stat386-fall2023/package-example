# TODO: Learn how to have GitHub run pytest

from mypackage import helpers
import numpy as np

def test_sum_to_one_row():
    """
    Test that rows are normalized properly.
    """
    x = np.array([[1, 1], [1, 3]])
    assert (helpers.sum_to_one(x, axis = 1) == np.array([[.5, .5], [.25, .75]])).all()

def test_sum_to_one_column():
    """
    Test that columns are normalized properly.
    """
    x = np.array([[1, 1], [1, 3]])
    assert (helpers.sum_to_one(x, axis = 0) == np.array([[.5, .25], [.5, .75]])).all()