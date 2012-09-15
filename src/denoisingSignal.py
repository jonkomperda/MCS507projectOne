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

if __name__ == '__main__':
    from numpy import *
    
    tone = readTone()
    n = len(tone)
    m = len(tone)/2
    print len(tone)
    F = fft.rfft(tone)
    
    p = lambda z: (abs(real(z)),abs(imag(z)))
    temp = p(F)
    
    plotIt(temp[0][:])
    
    for i in range(len(temp[0][:])):
        if temp[0][i] <= 40000:
            F[i] = 0
        if temp[1][i] <= 100000:
            F[i] = 0
        if i < 300:
            F[i] = 0
        if i > 10000:
            F[i] = 0
    plotIt(F)
    
    out = temp[0][:] + imag(temp[1][:])
    print out
    
    result = fft.irfft(F)
    #print len(result)
    #plotIt(temp)
    writeTone(result)