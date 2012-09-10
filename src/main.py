"""
MCS 507 Project One: the Fast Fourier Transform
The Fourier transform takes a signal from the time into the frequency domain. 
One application of the Fourier transform is that we can recover the amplitude
and frequencies of a sampled signal.

We will use the package numpy.fft. The underlying code for these functions is 
n f2c-translated and modified version of the FFTPACK routines. FFTPACK is a 
package of Fortran subprograms for the fast Fourier transform of periodic and 
other symmetric sequences. It includes complex, real, sine, cosine, and 
quarter-wave transforms.

For example, consider the signal 2*cos(4*2*pi*t) + 5*sin(10*2*pi*t) composed of 
a cosine with amplitude 2, frequency 4, and a sine with amplitude 5 and frequency
10. Using rfft of the package numpy.fft, the script below computes the discrete
Fourier transform on the real array of samples via the efficient Fast Fourier
Transform algorithm. We recover the amplitudes and corresponding frequencies of
the components of our signal. With matplotlib we plot the spectrum.
"""
import measureTime

# First we execute project one