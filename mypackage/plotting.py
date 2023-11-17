import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

def my_pca_plot(x, save_name, n_components = 2, y = None):
    """
    This function plots pairwise principal components in a grid of functions.

    Parameters
    ----------
    x : array_like
        Array to plot PCA

    save_name: string
        The filename or path/filename to save the figure

    n_components : int
        How many principal components to compute and plot

    y : array_like
        Array of labels used to color the plots.


    Returns
    -------
     None
    """

    pca_op = PCA(n_components = n_components)
    pca = pca_op.fit_transform(x)

    if y is not None:
        hue = y
    else:
        hue = None

    if n_components == 2:
        fig, axes = plt.subplots(1, 1)

        sns.scatterplot(x = pca[:, 0], y = pca[:, 1], hue = hue, ax = axes)
        fig.suptitle('PCA Plot')
        plt.savefig(save_name)


    if n_components == 3:
        fig, axes = plt.subplots(1, 3, figsize = (12, 4))
        sns.scatterplot(x = pca[:, 0], y = pca[:, 1], hue = hue, ax = axes[0])
        sns.scatterplot(x = pca[:, 0], y = pca[:, 2], hue = hue, ax = axes[1])
        sns.scatterplot(x = pca[:, 1], y = pca[:, 2], hue = hue, ax = axes[2])

        fig.suptitle('PCA Plot')
        plt.savefig(save_name)

    if n_components >= 4:
        raise ValueError('This function currently supports n_components = 2, 3.')



