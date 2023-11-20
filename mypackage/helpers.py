import pandas as pd

def sum_to_one(x, axis=1):
    """
    Normalize x so that the rows or columns sum to one.

    Parameters
    ----------
    x : array_like
        Array to normalize
    axis : int, optional
        Axis or axes along which a normalization is performed.
        The default, axis = 1, will row-normalize x.

    Returns
    -------
    row_normalized_array : ndarray
        An array with the same shape as `x`, with the specified
        axis removed. The array is normalized so the rows (axis = 1) or
        columns (axis = 0) sum to 1.

    Examples
    --------
    >>> sum_to_one(np.array([[1, 2], [3, 4]]))
    np.array([[.333333, .666667], [0.42857, 0.57142]])
    """

    if isinstance(x, pd.DataFrame):
        x = x.to_numpy()

    return x / x.sum(axis=axis, keepdims=True)


def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : int or float
        The first number to be added.
    b : int or float
        The second number to be added.

    Returns
    -------
    int or float
        The sum of the two input numbers.

    Examples
    --------
    >>> add(2, 3)
    5
    >>> add(1.5, 2.5)
    4.0
    """
    return a + b
