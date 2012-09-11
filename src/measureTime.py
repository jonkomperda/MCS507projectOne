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
    def __init__(self, startSample, endSample, n):
        self.start  = startSample
        self.end    = endSample
        self.count  = int((endSample-startSample)/n)
        
        self.mainLoop()
        
    def mainLoop(self):
        import numpy.random as rand
        self.x = x = arange(self.start, self.end, self.count)
        
        timed = timer()
        
        for i in x:
            signal = rand.random(i)
            timed()
            self.fftCalc(signal)
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
    a = assignmentOne(256,256000,100)
    a.plotTimes()
    
    #plt.plot(a.x,a.times)
    #plt.show()
    a.writeCSV()