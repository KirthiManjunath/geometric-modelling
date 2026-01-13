import numpy as np

class hermite:
    def __init__(self, p1, m1 = 0, p0 = 0, m0 = 0, prev = None):
        self.p0 = p0
        self.p1 = p1
        self.m0 = m0
        self.m1 = m1
        self.prev = prev
        self.C2continuity()

    def hermite_basis(self):
        t = np.arange(0,1.01,0.01)
        h1 = 2*t**3 - 3*t**2 + 1
        h2 = -2*t**3 + 3*t**2 
        h3 = t**3 -2*t**2 + t
        h4 = t**3 -t**2
        return h1*self.p0 + h2*self.p1 + h3*self.m0 + h4*self.m1  
    
    def C2continuity(self):
        if self.prev == None:
            return
        else:
            self.p0 = self.prev.p1 #C0 continuity
            self.m0 = self.prev.m1 #C1 continuity
            self.m1 = 3*self.p1 - 3*self.prev.p0 - self.prev.m0 - 4*self.m0 #C2 continuity
        self.m1 = self.m1 / self.prev.m1 if self.prev.m1!= 0 else 1
        
    
    


    