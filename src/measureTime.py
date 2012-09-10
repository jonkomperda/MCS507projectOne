"""
Assignment One: measuring the CPU time

The cost of the Fast Fourier Transform algorithm on a data set of dimension 
'n' is proportional to nlog_2(n). The purpose of this assignment is to 
experimentally determine whether the running time of the implmentation
of the FFT algorithm in the package numpy.fft is indeed O(nlog_2(n)).

"""
from numpy import *
class assignmentOne():
    isTimed = False
    
    def __init__(self):
        pass
    
    def timer(self):
        import time
        if self.isTimed:
            stopTime    = time.clock()
            totalTime   = stopTime = self.startTime
            print 'Total runtime: '+ str(totalTime) + ' seconds'
            return totalTime
        else:
            self.startTime  = time.clock()
            self.isTimed = True
    
    def fftSim(self,samples):
        import numpy.random
        s = random(samples)
        F = fft.rfft(s)
        m = samples/2
        p = lambda z: (abs(real(z))/m,abs(imag(z))/m)
        t = p(F)
        tol = 1.0e-8
        for i in range(0,len(t[0])):
            str(t[0][i]) if t[0][i] >= tol
            str(t[1][i]) if t[1][i] >= tol

if __name__ == '__main__':
    """
    This is the testing block of code
    """
    first = assignmentOne()
    start = first.timer()
    end = first.timer()

        