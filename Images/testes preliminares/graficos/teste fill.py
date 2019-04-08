#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 1.01, 0.01)
s = np.sin(2*2*np.pi*t)
s1 = s*np.exp(-5*t)

plt.fill(t, s1, 'r')
plt.grid(True)
plt.show()
