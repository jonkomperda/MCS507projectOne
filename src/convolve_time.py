"""
The Fourier transform turns a convolution into a componentwise product. Interpreting the arrays as the
coefficient vectors of two polynomials (the ith entry is the coefficient of xi), the convolution of the coefficient
vectors gives the coefficient vector of the product of the two polynomials. Using the fast FFT, the O(n**2)
operation becomes O(n log2(n)).


Write a python script to demonstrate the benefit of performing a convolution using the FFT, using timings
on sufficiently large arrays. Note that signal package of scipy contains the function fftconvolve.
"""

import numpy as np
from numpy.fft import rfft, irfft
from scipy.signal import fftconvolve
from objTimer import *
import random
import matplotlib.pyplot as plt
from math import log
from scipy.optimize import leastsq

def residuals(alpha,observed,expected):
            return observed-alpha*expected


# Number of iterations
n=200

# Number of observations to test
start=5
count=10
x = np.array([(2**j)*start for j in range(count+1)])



# Generate random vectors 
a=np.array([random.randint(0,10) for i in range(1,max(x))])
b=np.array([random.randint(0,10) for i in range(1,max(x))])


times1=[]

timed=timer()
for i in x:
    timed()
    for j in range(1,n):
        np.convolve(a[:i],b[:i])
    t=timed()
    times1.append(t)
    
plt.plot(x,times1)
plt.show()        


times2=[]

timed=timer()
for i in x:
    timed()
    for j in range(1,n):
        fftconvolve(a[:i],b[:i])
    t=timed()
    times2.append(t)



plt.plot(x,times2)
plt.show()

# Calc expected times for convolve
expected1 = np.array([i**2 for i in x])
observed1 = times1
p0=.001

W = leastsq(residuals,p0,args=(observed1,expected1), maxfev=100000, full_output=1)
expected_adjusted1 = [float(W[0])*expected1[i] for i in range(len(expected1))]

p1 = plt.plot(x,times1,'b:',label='Actual Times')
p2 = plt.plot(x,expected_adjusted1,'r--', label='Expected Times')
plt.legend(['Actual','Expected'], loc='upper left')
plt.show()



# Calc expected times for FFT
expected2 = np.array([log(i,2.0)*i for i in x])
observed2 = times2
p0=.001
# Note: it looks like I need to add an intercept term here
W = leastsq(residuals,p0,args=(observed2,expected2), maxfev=100000, full_output=1)
expected_adjusted2 = [float(W[0])*expected2[i] for i in range(len(expected2))]

p1 = plt.plot(x,times2,'b:',label='Actual Times')
p2 = plt.plot(x,expected_adjusted2,'r--', label='Expected Times')
plt.legend(['Actual','Expected'], loc='upper left')
plt.show()


    


