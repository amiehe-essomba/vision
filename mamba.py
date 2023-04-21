import numpy as np
import matplotlib.pyplot as plt


R = 8.14
F = 9.648533289e+4
ep_rr = 9.4#12
T = 300 
ep_0 = epsilon = 8.854e-12
A = 0.66
C0 = (ep_0 * ep_rr * R * T) / (2 * (F * A ) ** 2)

gama = 1
sigma = 5
Kb = 1.380649e-23

a = -50
b = 50
N = 100
dx = (b-a)/N 

V = [a]
W = []
for i in range(N):
	a += dx  
	B = a * sigma# / (Kb * T)
	
	V.append(a)
	W.append(B)
	
V = np.array(V)
W = np.array(W)

Q = [0]
for i in range(N):
	Q_M = 2 * F * C0 * A * np.sign(W[i]) * np.sqrt( 2 /  gama ) #* np.sqrt(np.log(1 + 2 * np.sinh( W[i] ) * np.sinh( W[i] ) ))
	
	Q.append(Q_M)

print(Q)
plt.plot(V, Q)
plt.show()
