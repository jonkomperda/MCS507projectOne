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
#import measureTime
from Tkinter import *
import tkMessageBox


class App(Frame):
    def __init__(self,master):
        """
        Initialize base class
        Draws the window and loads our project
        """
        Frame.__init__(self,master)
        
        # Initialize the body of the window
        self.bodyInit(master)
        
        # Creates the menus
        self.menuInit(master)
        
    
    def bodyInit(self,master):
        #window properties
        master.wm_state("zoomed")
        self.master.title("MCS507 Project One")
        
    
    def menuInit(self,master):
        self.menu = Menu(self)
        self.master.config(menu=self.menu)
        
        # Help menu
        self.helpMenu = Menu(self.menu)
        self.menu.add_cascade(label='Help',menu=self.helpMenu)
        self.helpMenu.add_command(label='About', command = self.about)
    
    def about(self):
        tkMessageBox.showinfo('About', 'Authors: Jon Komperda\
                                               \nAdam McElhinney')

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
        