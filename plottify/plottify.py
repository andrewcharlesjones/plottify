import matplotlib.pyplot as plt
from matplotlib import collections
from matplotlib.lines import Line2D


def autosize(fig=None, figsize=None):

    ## Take current figure if no figure provided
    if fig is None:
        fig = plt.gcf()

    if figsize is None:

        ## Get size of figure
        figsize = fig.get_size_inches()
    else:

        ## Set size of figure
        fig.set_size_inches(figsize)

    ## Set sizes of objects
    ##      -- Note that this function currently adjusts sizes only
    ##         according to the horizontal width fo the figure.

    ## Font sizes
    fontsize_labels = figsize[0] * 5
    fontsize_ticks = fontsize_labels / 2

    ## Scatter point size
    scatter_size = (figsize[0] * 1.5) ** 2

    ## Line width
    linewidth = figsize[0]

    ## Spine width
    spine_width = 0.16 * figsize[0]

    ## Tick length and width
    tick_length = spine_width*8
    tick_width = spine_width

    ## Change all of these sizes
    axes = fig.get_axes()
    for ax in axes:

        ## Set label font sizes
        for item in [ax.title, ax.xaxis.label, ax.yaxis.label]:
            item.set_fontsize(fontsize_labels)

        ## Set tick font sizes
        for item in ax.get_xticklabels() + ax.get_yticklabels():
            item.set_fontsize(fontsize_ticks)

        ## Set line widths
        plot_objs = [child for child in ax.get_children() if isinstance(child, Line2D)]
        for plot_obj in plot_objs:
            plot_obj.set_linewidth(linewidth)

        ## Set scatter point sizes
        plot_objs = [
            child
            for child in ax.get_children()
            if isinstance(child, collections.PathCollection)
        ]
        for plot_obj in plot_objs:
            plot_obj.set_sizes([scatter_size])

        ## Set spine widths
        for spine in ax.spines.values():
            spine.set_linewidth(spine_width)

        ## Set tick width and length
        ax.tick_params(width=tick_width, length=tick_length)

    ## Set tight layout
    plt.tight_layout()

if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    n = 100
    x = np.random.uniform(low=-5, high=5, size=n)
    y = x + np.random.normal(scale=0.5, size=n)

    for size in [3, 10, 20]:

        plt.figure(figsize=(size, size))
        plt.scatter(x, y)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Default")
        plt.show()

        plt.figure(figsize=(size, size))
        plt.scatter(x, y)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Autosized")
        autosize()
        plt.show()
