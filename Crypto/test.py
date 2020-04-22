import scipy.stats as s
import numpy as np
import matplotlib.pyplot as plt


def weib(x, n, a): return (a / n) * (x / n) ** (a - 1) * np.exp(-(x / n) ** a)


data = np.loadtxt("stack_data.csv")
(loc, scale) = s.exponweib.fit_loc_scale(data, 1, 1)
print(loc, scale)
x = np.linspace(data.min(), data.max(), 1000)
plt.plot(x, weib(x, loc, scale))
plt.hist(data, data.max(), normed=True)
plt.show()
