"""
Modification of his original program to determine the purpose
of padding with zeros. Based on this program, I appears that so long as you
are using the fftconvolve function from scipy and not doing the convolution
explicitly, then you do NOT need to pad with zeros.
"""

import numpy as np
from numpy.fft import rfft, irfft
#a = np.array([1,2,3,4,0,0,0,0])
#b = np.array([3,4,9,8,0,0,0,0])
a = np.array([1,2,3,4])
b = np.array([3,4,9,8])


print np.convolve(a,b)
A = rfft(a); B = rfft(b)
C = A*B
print irfft(C)


from scipy.signal import fftconvolve
print fftconvolve(a,b) 
