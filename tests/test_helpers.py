from my_package import helpers
import numpy as np

def test_sum_to_one_row():
    x = np.array([[1, 1], [1, 3]])
    assert (helpers.sum_to_one(x, axis = 1) == np.array([[.5, .5], [.25, .75]])).all()

def test_sum_to_one_column():
    x = np.array([[1, 1], [1, 3]])
    assert (helpers.sum_to_one(x, axis = 0) == np.array([[.5, .25], [.5, .75]])).all()