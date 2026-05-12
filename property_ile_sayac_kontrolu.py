class main:
    def __init__(self):
        self.counter = 0
        self.state = True
        self.maximum_countper = 256
        
        
    def loop(self):
        while self.state:
            if self. counter > self.maximum_countper:
                self.stateProp = False
            else:
                print(self.counter)
                self.counter += 1
                
    @property
    def stateProp(self):
        return self.state
     
    @stateProp.setter
    def stateProp(self, state):
        print(state) 
        self.state = state
        return self.state
         
clss = main()

clss.loop() 