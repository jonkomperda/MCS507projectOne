from scipy.io import wavfile
from numpy import *
from scitools.sound import *
import matplotlib.pyplot as plt

inFile = './static_noise_test.wav'

w = wavfile.read(inFile) #index 0 is sample rate, 1 is array, 2 is dtype

soundArray = w[1]

F = fft.rfft(soundArray)

def filt(x): 
    if abs(x) >= 10000:
        return x #this is the filter function
    else:
        return 0

out = filter(filt,F)
#out = F
iF = fft.irfft(out)
print iF
iF = array( [int(x) for x in iF ])
print type(iF)

#plt.plot(out,'r--')
#plt.show()

play(iF)


#print [i for i in array]