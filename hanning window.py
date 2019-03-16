import numpy as np
import matplotlib.pyplot as mp
m=int(input("enter a m value:"))
h=[]
for n in range(0,m-1):
	x1=np.cos(2*3.14*n/(m-1))
	x=0.5-0.5*x1
	h=np.append(h,x)
mp.stem(h)
mp.xlabel("n")
mp.ylabel("w")
mp.plot("hanning window")
mp.show()
