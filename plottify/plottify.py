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

    ## Make font sizes proportional to figure size
    fontsize_labels = figsize[0] * 5
    fontsize_ticks = fontsize_labels / 2
    axes = fig.get_axes()
    for ax in axes:

        ## Set label font sizes
        for item in [ax.title, ax.xaxis.label, ax.yaxis.label]:
            item.set_fontsize(fontsize_labels)

        ## Set tick font sizes
        for item in ax.get_xticklabels() + ax.get_yticklabels():
            item.set_fontsize(fontsize_ticks)

        ## Set line widths
        linewidth = figsize[0]
        plot_objs = [child for child in ax.get_children() if isinstance(child, Line2D)]
        for plot_obj in plot_objs:
            plot_obj.set_linewidth(linewidth)

        ## Set scatter point sizes
        scatter_size = figsize[0] * 13
        plot_objs = [
            child
            for child in ax.get_children()
            if isinstance(child, collections.PathCollection)
        ]
        for plot_obj in plot_objs:
            plot_obj.set_sizes([scatter_size])

    ## Set tight layout
    plt.tight_layout()
