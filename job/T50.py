import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def gaussian(x, a, x0, sigma):
    return a * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))


x = np.linspace(-10, 10, 100)
y = gaussian(x, 1, 0, 1) + 0.1 * np.random.normal(size=len(x))

popt, pcov = curve_fit(gaussian, x, y, p0=[1, 0, 1])

plt.plot(x, y, 'b+:', label='data')
plt.plot(x, gaussian(x, *popt), 'r-', label='fit')
plt.legend()
plt.title('Gaussian fit')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
