import numpy as np
import matplotlib.pyplot as plt
m=int(input("enter a m value:"))
h=[]
for n in range(0,m-1):
	x1=np.cos(2*3.14*n/(m-1))
	x=0.54-0.46*x1
	h=np.append(h,x)
plt.stem(h)
plt.xlabel("n")
plt.ylabel("w")
plt.plot("hamming window")
plt.show()
