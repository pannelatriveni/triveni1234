import numpy as np
import matplotlib.pyplot as plt
m=int(input("enter a m value:"))
h=[]
for n in range(0,m-1):
	x1=np.abs(n-(m-1)/2)
	x=1-((2*x1)/(m-1))
	h=np.append(h,x)
plt.stem(h)
plt.xlabel("n")
plt.ylabel("w")
plt.plot("tringular window")
plt.show()
