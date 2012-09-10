"""
Assignment One: measuring the CPU time

The cost of the Fast Fourier Transform algorithm on a data set of dimension 
'n' is proportional to nlog_2(n). The purpose of this assignment is to 
experimentally determine whether the running time of the implmentation
of the FFT algorithm in the package numpy.fft is indeed O(nlog_2(n)).

"""
from numpy import *
from objTimer import *

class assignmentOne():
    isTimed = False
    
    def __init__(self, samples):
        import numpy.random as r
        self.s = r.random(samples)
        
        timeIt = timer()
        timeIt()
        self.fftSim(samples)
        timeIt()
        print timeIt
        
    
    def fftSim(self,samples):
        self.F = fft.rfft(self.s)
        self.m = samples/2
        p = lambda z: (abs(real(z))/self.m,abs(imag(z))/self.m)
        self.t = p(self.F)
        tol = 1.0e-8
        #for i in range(0,len(self.t[0])):
            #if self.t[0][i] >= tol: print str(self.t[0][i]) 
            #if self.t[1][i] >= tol: print str(self.t[1][i]) 
            #pass
    
    def plotIt(self):
        import matplotlib.pyplot as plt
        plt.plot(abs(self.F)/self.m)
        plt.show()

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    """
    This is the testing block of code
    """
    z = []
    x = arange(10000,20001,10000)
    print x
    z = [assignmentOne(i) for i in x]
    
    
    #plt.plot(x,y)
    #plt.show()