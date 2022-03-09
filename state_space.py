import numpy as np
import control 
import matplotlib.pyplot as plt

m = 10
k = 4 # spring const
d = 2 # damping const

A = np.array([[0,1],[-k/m,-d/m]])
B = np.array([[0],[1/m]])
C = np.array([[1,0]])
D = np.array([[0]])

S = control.ss(A,B,C,D)

print(S)

t0 = 0
t1 = 50
dt = 0.01
nt = int(t1/dt) + 1
t = np.linspace(t0,t1,nt)
F = 10*np.ones(nt)

x0 = np.array([1, 0])

(t,y,x) = control.forced_response(S, t, F, x0,return_x=True)

x1 = x[0,:]
x2 = x[1,:]


plt.close("all")
plt.figure(1,figsize=(12 , 9))
plt.subplot(3,1,1)
plt.plot(t,x1,"blue")
plt.grid()
plt.legend(labels=("x1[m]",))
plt.subplot(3,1,2)
plt.plot(t,x2,"green")
plt.grid()
plt.legend(labels=("x2[m/s]",))
plt.subplot(3 , 1 , 3)
plt.plot(t,F,"red")
plt.grid()
plt.legend(labels=( "F[N]" ,))
plt.xlabel("t[s]")
plt.show()

H1 = control.ss2tf(S)
print(H1)

C2 = np.array([[0,1]])
S2 = control.ss(A,B,C2,D)
H2 = control.ss2tf(S2)
print("--H2--")
print(H2)