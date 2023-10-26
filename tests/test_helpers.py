from ..my_package import helpers
import numpy as np

def test_sum_to_one():
    x = np.array([[1, 1], [1, 3]])
    assert helpers.sum_to_one(x) == np.array([[.5, .5], [.25, .75]])