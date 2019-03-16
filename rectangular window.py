import numpy as np
import matplotlib.pyplot as plt
m=int(input("enter a value of m:"))
h=[]
for n in range(0,m-1):
	x=1
	h=np.append(h,x)
	
plt.stem(h)
plt.xlabel("n")
plt.ylabel("w")
plt.title("rectangular window")
plt.show()
