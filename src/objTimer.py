class timer():
    isTimed = False
    totalTime = 0
    
    def __init__(self):
        pass
        
    def __call__(self):
        self.timer()
    
    def __str__(self):
        string = 'Total runtime: '+ str(self.totalTime) + ' seconds'
        return string
        
    def timer(self):
        import time
        if self.isTimed:
            stopTime    = time.clock()
            self.totalTime   = stopTime = self.startTime
            
        else:
            self.startTime  = time.clock()
            self.isTimed = True
    
tim = timer()

tim()

tim()

print tim

jon = timer()
jon()
for i in range(100000000):
    pass
jon()

print jon