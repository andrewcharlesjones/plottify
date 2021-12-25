import numpy as np
from plottify import autosize
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
    plt.savefig("./plots/scatterplot{}{}_default.png".format(size, size))
    plt.show()

    plt.figure(figsize=(size, size))
    plt.scatter(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Autosized")
    autosize()
    plt.savefig("./plots/scatterplot{}{}_autosized.png".format(size, size))
    plt.show()

# plt.scatter(x, y)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Autosized")
# autosize(figsize=(3, 3))
# plt.savefig("./plots/scatterplot33_autosized.png")
# plt.show()


# plt.figure(figsize=(5, 5))
# plt.scatter(x, y)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Default")
# plt.savefig("./plots/scatterplot55_default.png")
# plt.show()

# plt.scatter(x, y)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Autosized")
# autosize(figsize=(5, 5))
# plt.savefig("./plots/scatterplot55_autosized.png")
# plt.show()