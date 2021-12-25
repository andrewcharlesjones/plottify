# plottify

The plottify package is intended to easily make plots more legible. It's a thin wrapper around [matplotlib](https://matplotlib.org/) that automatically adjusts font sizes, scatter point sizes, line widths, etc. according to the figure size.

By default, matplotlib sets the sizes of these objects to pre-specified values, regardless of the figure size. This can result in tiny fonts or sizes for larger figures:

![scatterplot2020_default](examples/plots/scatterplot2020_default.png)

Plottify's `autosize` function adjusts these sizes automatically to make them more legible:

![scatterplot33_autosized](examples/plots/scatterplot33_autosized.png)

![scatterplot1010_autosized](examples/plots/scatterplot1010_autosized.png)

![scatterplot2020_autosized](examples/plots/scatterplot2020_autosized.png)

## Bugs and feature requests

Please report any bugs or feature requests as a GitHub issue.
