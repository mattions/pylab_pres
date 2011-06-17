# fitting_data.py
# Proper importing style

import numpy as np
import scipy as sp
import matplotlib
import matplotlib.mlab
import matplotlib.pyplot as plt

# Importing the data

try:
   data = matplotlib.mlab.csv2rec('data.txt')
   "Data loaded"

except:
   print "Bad luck. Where is the file?"
   
plt.plot(data.x, data.y, 'ko', label='data')

# Fitting
polycoeffs = np.polyfit(data.x, data.y, 1)
p1 = np.poly1d(polycoeffs)
plt.plot(data.x, p1(data.x), label='fit')

plt.title('Quick overview of the data')
plt.xlabel('Time [s]')
plt.ylabel('Concentration [mM]')
plt.legend(loc=0)
# Line to show the figure
plt.show()
