def plotIt(data):
    import matplotlib.pyplot as plt
    plt.plot(data)
    plt.show()

def readTone():
    from scipy.io import wavfile
    
    inFile = './static_noise_test.wav'
    
    tone = wavfile.read(inFile)
    return tone[1]
    
def writeTone(data):
    from scitools.sound import write
    
    write(data,'meow.wav')

def filterFFT(data,ampfiltreal=40000,ampfiltimag=100000,highpass=300,lowpass=10000):
    p = lambda z: (abs(real(z)),abs(imag(z)))
    temp = p(data)
    
    for i in range(len(temp[0][:])):
        if temp[0][i] <= ampfiltreal:
            data[i] = 0
        else:
            data[i] *= 10
        if temp[1][i] <= ampfiltimag:
            data[i] = 0
        if i < highpass:
            data[i] = 0
        if i > lowpass:
            data[i] = 0
    return data

if __name__ == '__main__':
    from numpy import *
    
    tone = readTone()

    F = fft.rfft(tone)

    F = filterFFT(F)

    result = fft.irfft(F)

    writeTone(result)