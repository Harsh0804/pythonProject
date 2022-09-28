class Number:

    Multiplier = None

    def __init__(self,x,y):
        self.x=x
        self.y=y

    #subpart 1
    def add(self):
        return self.x+self.y

    #subpart 2
    @classmethod
    def multiply(cls,a):
        return  a* cls.Multiplier

    @staticmethod
    def subtract(b,c):
        return b-c

    def value(self):
        return(self.x,self.y)







obj=Number(5,10)
print(obj.add())
print(Number.Multiply(10))
print(number.subtract(100,1))

