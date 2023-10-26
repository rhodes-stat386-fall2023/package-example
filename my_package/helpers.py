import numpy as np

def sum_to_one(x, axis = 1):
    """
    Parameters
    ----------
        x : array_like
        Array to normalize
    axis : int, optional
        Axis or axes along which a normalization is performed.  The default,
        axis = 1, will row-normalize x.

    Returns
    -------
    row_normalized_array : ndarray
        An array with the same shape as `x`, with the specified
        axis removed. The array is normalized so the rows (axis = 0) or columns (axis = 1) sum to 1.

    Examples
    --------
    >>> sum_to_one(np.array([[1, 2], [3, 4]]))
    np.array([[.333333, .666667], [0.42857, 0.57142]])
    """
    return x / np.sum(x, axis = axis)
