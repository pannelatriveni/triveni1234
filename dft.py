from pylab import*
import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
x=int(input("enter the x[n]:"))
for j in range(x):
	a=int(input("enter the values:"))
	x=np.append(a,x)
N=int(input("enter a no.of samples:"))
j=cm.sqrt(-1)
X=[]
w=np.linspace(-np.pi,np.pi,N)
for i in range(0,N):
	sum=0
	for n in range(0,len(x)):
		sum=sum+(x[n]*np.exp((-2*np.pi*n*w[i]*j)/N))
	X.append(sum)
plt.subplot(221)
plt.plot(w,np.abs(X))
plt.xlabel('frequency(w/pi)')
plt.ylabel('magnitude')
plt.title('magnitude spectrum')
plt.grid()
plt.subplot(212)
plt.plot(w,angle(X)/np.pi)
plt.xlabel('frequency(w/pi)')
plt.ylabel('phase angle in radian')
plt.title('phase spectrum')
plt.grid()
plt.show()
    