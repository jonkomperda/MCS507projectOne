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
    times = []
    def __init__(self, startSample, iterations, n):

        #Constructor for the assignment

        self.start  = startSample
        #self.count  = int((endSample-startSample)/n)
        self.loops= iterations
        self.count  = n
        
        self.mainLoop()
        
    def mainLoop(self):
        import numpy.random as rand
        # Array containing the number of samples to compute
        # Per the question, "random data of increasing size n (doubling the value
        # for n each time)"        
        #self.x = x = arange(self.start, self.end, self.count)
        self.x = x = array([(2**j)*self.start for j in range(self.count+1)])
        
        # I think that a static set of random data needs to be generated first
        # Can't have count >~10 or will get error saying max dimension exceeded
        data_seed=rand.random(max(self.x))
        # I think that the computation time is proportional to n*log_2(n)
        # only if its the same signal and computation
        f = lambda t: 2*cos(4*2*pi*t) + 5*sin(10*2*pi*t)
        total_signal=f(data_seed)
        timed = timer()

        # I think we may need to loop this some more
        
        for i in x:
            timed()
            for j in range(1,self.loops):
                #signal = rand.random(i)
                #signal=f(arange(0.0,1.0,1.0/i))
                self.signal=total_signal[:i]
                self.fftCalc(self.signal)
            t = timed()
            self.times.append(t)
            
            
            
        print self.times
        
    def fftCalc(self,signal):
        self.F = fft.rfft(signal)
        #self.m, m = len(signal)/2, len(signal)/2
        #p = lambda z: (abs(real(z))/m,abs(imag(z))/m)
        #self.t = p(self.F)
        
    def plotFFT(self):
        import matplotlib.pyplot as plt
        plt.plot(abs(self.F)/self.m)
        plt.show()
    
    def plotTimes(self):
        import matplotlib.pyplot as plt
        #nlog2y = [i for i in self.x*(log(self.x)/log(2.0))]
        
        plt.plot(self.x,self.times)
        plt.show()
        
    def writeCSV(self):
        import csv
        writer = csv.writer(open('timings.csv', 'wb'), delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Samples,Time'])
        for i in range(len(self.times)):
            writer.writerow([self.x[i],self.times[i]])
       
        
        
        
        
        
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    #a = assignmentOne(256,256000,100)
    #a = assignmentOne(256,256*10**2,100)
    a = assignmentOne(256,1000,10)
    a.plotTimes()
    
    #plt.plot(a.x,a.times)
    #plt.show()
    #a.plotFFT()
    a.writeCSV()


# Calcuate the raw expected times, then the fitted expected times
from math import log
from scipy.optimize import leastsq

expected=array([log(i,2.0)*i for i in a.x])
observed=a.times

def residuals(alpha,observed,expected):
    #resid=observed-alpha*expected
    #return resid
    return observed-alpha*expected

p0=.001

W=leastsq(residuals, p0, args=(observed, expected), maxfev=100000, full_output=1)







