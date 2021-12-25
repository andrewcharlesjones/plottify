import numpy as np

n = 100
x = np.linspace(-5, 5, n)
y = x**2
fig, ax = plt.subplots(figsize=(5, 5))
ax.plot(x, y)
ax.set_xlabel("X")
ax.set_ylabel("Y")
autosize(fig)
plt.show()

