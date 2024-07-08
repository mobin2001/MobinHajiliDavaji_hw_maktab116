class Add(int):
    
    def __init__(self,a):
        
        self.a = a
        print(self.a)

    def __call__(self, number):
        
        self.a += number 
        print(self.a)
        return self 


Add(10)(11)(12)

