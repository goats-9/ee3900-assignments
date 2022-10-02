import numpy as np
from matplotlib import pyplot as plt

def unitstep(t):
    if (t < 0): return 0
    elif (t == 0):return 0.5
    else: return 1

def v1(t):
    if (t >= 0): return 2/3*(1 + np.exp(-t*1.5e6))*unitstep(t)
    else: return 0

vc0 = np.vectorize(v1, otypes=['double'])

t = np.linspace(0, 1e-5, 1000000)
plt.plot(t, vc0(t))
plt.xlabel('t (s)')
plt.ylabel('$v_{C_0}(t)$ (V)')
plt.grid()
plt.savefig('../figs/3_4.png')
