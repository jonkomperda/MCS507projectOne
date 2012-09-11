class timer():
    isTimed = False
    totalTime = 0
    
    def __init__(self):
        pass
    
    def __new__(self):
        pass
    
    def __call__(self):
        return self.timer()
        
    def __str__(self):
        string = 'Total runtime: '+ str(self.totalTime) + ' seconds'
        return string
        
    def timer(self):
        import time
        if self.isTimed:
            print 'Stop Timer...'
            stopTime    = time.clock()
            self.totalTime   = stopTime - self.startTime
            self.isTimed = False
            return self.totalTime
            
        else:
            print 'Start Timer...'
            self.startTime  = time.clock()
            self.isTimed = True
            self.totalTime = 0
            return 0.0

if __name__ == '__main__':
    tim = timer()
    tim()
    tim()
    print tim
    jon = timer()
    jon()
    for i in range(10000000):
        pass
    jon()
    print jon
    moo = timer()
    moo()
    moo()
    print moo
    
    a = tim()
    print a