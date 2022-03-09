import numpy as np
import control 
import matplotlib.pyplot as plt

wb = 1 #bandwidth
H = control.tf([1], [1/wb , 1]) # tf of a Low pass filter of cutoff at wb
print(H)
w0 = 0.1
w1 = 10
dw = 0.001
nw = int((w1-w0)/dw) + 1 # samples

w = np.linspace(w0,w1,nw)

(mag,phase_rad,w) = control.bode_plot(H , w )

plt.close("all")
plt.figure(1 , figsize =(12 , 9))
plt.subplot(2 , 1 , 1)
plt.plot(np.log10(w) , mag , "blue")
# plt . xlabel ( " w [ rad / s ] ")
plt.grid()
plt.legend(labels =( "mag",))
plt.subplot(2 , 1 , 2)
plt.plot(np.log10(w),phase_rad*180/np.pi,"green")
plt.xlabel( "w[rad/s]")
plt.grid()
plt.legend(labels =( " phase [ deg ] " ,))
plt.show()
