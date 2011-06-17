
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from numpy import exp

x = np.linspace(0,10)
plt.title('Exponatial decay')
plt.plot(x, exp(-x))
plt.show()

