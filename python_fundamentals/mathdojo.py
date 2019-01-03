class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self,num,*vals):
        for i in vals:
            num+=i
        self.result += num
        return self
    
    
    def subtract(self,num,*vals):
        for i in vals:
            num+=i
        self.result -= num
        return self


md=MathDojo()

x=md.add(2).add(2,5,1).subtract(3,2).result
print(x)