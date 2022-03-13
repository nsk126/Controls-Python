import numpy as np
import control 
import matplotlib.pyplot as plt

# PLANT

# wb = 1 #bandwidth
# H = control.tf([1], [1/wb , 0]) # tf of a Low pass filter of cutoff at wb
# # this is now a intergrator plant
H = control.tf([10],[1,10])
print(H)


KI = control.tf([5,25],[1,0])
KPID = control.tf([10,2500],[1,2500]); 
P = control.tf([5],[1])

PID = control.series(KI,KPID);
H1 = control.series(H,PID)
# H1 = control.series(H,P)
H1 = control.feedback(H1,[1],-1) # arg2 = [1], unit feedback
print(H1)


# Frequency range
w0 = 0.1
w1 = 1000
dw = 0.01 
nw = int((w1-w0)/dw) + 1 # samples
w = np.linspace(w0,w1,nw)

# Time range
t = np.linspace(0,1.4,1000)

# Frequency & Time plots
(mag,phase_rad,w) = control.bode_plot(H , w )
(t, y) = control.step_response(H1,t)
(mag1,phase_rad1,w) = control.bode_plot(H1 , w )


plt.close("all")

plt.figure(1 , figsize =(12 , 9))
# plt.figure()
plt.subplot(3 , 1 , 1)
plt.plot(np.log10(w) , 20*np.log10(mag) , "r")
plt.plot(np.log10(w) , 20*np.log10(mag1) , "b")

plt.ylabel("mag(dB)")
# plt . xlabel ( " w [ rad / s ] ")
plt.grid()
plt.legend(labels =( "Open loop","Integrator"))
plt.subplot(3 , 1 , 2)
plt.plot(np.log10(w),phase_rad*180/np.pi,"green")
plt.xlabel( "w[rad/s]")
plt.grid()
plt.legend(labels =( "phase[deg]" ,))
# plt.show()

plt.subplot(3 , 1 , 3)
plt.plot(t,y)
plt.xlabel("t[s]")
plt.grid()
plt.show()
