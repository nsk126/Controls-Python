import numpy as np
import control 
import matplotlib.pyplot as plt

(num_pade, den_pade) = control.pade(5,2) # T = 5 n = 2
# T is time delay
# n is order of pade approximation
 
H = control.tf(num_pade, den_pade)

num = np.array([1])
den = np.array([10, 1])

H_wo = control.tf(num,den)

H_w = control.series(H, H_wo)

t = np.linspace(0,40,1000)

(t,y) = control.step_response(H_w, t)

plt.plot(t,y)
plt.xlabel("t[s]")
plt.grid()
plt.show()