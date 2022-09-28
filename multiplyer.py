class Number:
    Multiplier = None

    def __init__(self,x,y):
        self.x=x
        self.y=yield

    #subpart 1
    def add(self):
        return self.x+self.y

    #subpart 2
    @classmethod
    def multiply(cls,a):
        return  a* cls.Multiplier






    obj=Number()
    print(obj.add(5,10))
    print(Number.Multiply(10))

