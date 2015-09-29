class JuliaSet(object):

    def __init__(self, c, n=100):
        self.c = c
        self.n = n
        self._d = 0.001
        self._complexplane=[]
        self.set=[]

    def juliamap(self, z):
        return z**2 + self.c

    def iterate(self, z):
        m = 0
        while True:
            z = self.juliamap(z)
            m +=1
            if abs(z)>2:
                return m
            elif m>=self.n:
                return 0
    
    def drange(self, start, stop, step):
        r = start
        while r <= stop:
            yield r
            r += step
    
    # Generate evenly spaced values over x and y planes
    def get_complexplane(self):
        self._complexplane = []
        _range=self.drange(-2, 2, self._d)
        for x in self.drange(-2, 2, self._d):
            for y in self.drange(-2, 2, self._d):
                self._complexplane.append(complex(x,y))
    
    def set_spacing(self, d):
        self._d = d
        self.get_complexplane()
        
    def generate(self):
        self.set = [self.iterate(x) for x in self._complexplane]
        return self.set
