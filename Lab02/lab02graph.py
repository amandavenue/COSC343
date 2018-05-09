import numpy as np
import matplotlib.pyplot as plt
import os, inspect

workingDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
npzfile = np.load(os.path.join(workingDir, "t1dataset1.npz"))

x = npzfile['x']
y = npzfile['y']

x2 = np.linspace (-5, 5, 40)
y2 = 0.2*x2**2 + 0.2*x2 -2.1

plt.close('all')
plt.figure()

plt.plot(x, y, 'g.')
plt.plot(x2, y2, 'r-')

plt.legend(['sample data', 'my function'])
plt.xlabel('x')
plt.ylabel('y')

plt.show()