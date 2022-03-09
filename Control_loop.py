import numpy as np
import control 
import matplotlib.pyplot as plt

# system = 1/s*(s+1)^2
# Controller: P gain = 1
S = control.tf([1], [1,2,1,0])
C = control.tf([1], [1])
L = control.series(C,S)

w0 = 0.1
w1 = 10
dw = 0.001
nw = int((w1-w0)/dw) + 1 # samples

w = np.linspace(w0,w1,nw)

plt.close('all')
plt.figure(1, figsize=(12,9))

(mag, phase_rad, w) = control.bode_plot(L, w, dB=True, deg=True, margins=True)

(GM, PM, wg, wp) = control.margin(L)

print("%.2f" % GM)
print("%.2f" % PM)
print("%.2f" % wg)
print("%.2f" % wp)

plt.show()