from scipy.io import wavfile
from numpy import *
import matplotlib.pyplot as plt

inFile = './static_noise_test.wav'

w = wavfile.read(inFile) #index 0 is sample rate, 1 is array, 2 is dtype

soundArray = w[1]

F = fft.rfft(soundArray)

def filt(x): return x >= 1000000 #this is the filter function

out = filter(filt,F)

plt.plot(out,'r--')
plt.show()

wavfile.write('outfile.wav',44100,out)


#print [i for i in array]