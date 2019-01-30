import matplotlib.pyplot as mp
import numpy as np
fs=int(input("enter a sampling frequency"))
f=int(input("enter a frequency"))
t=int(input("enter a time"))
x = np.arange(t)
y = np.sin(2 * np.pi * f * x/ fs)
mp.plot(x, y)
mp.xlabel('time(samples)')
mp.ylabel('amplitude')
mp.show()