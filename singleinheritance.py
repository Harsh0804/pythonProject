class Person:
    def  A (self):
        self.name=input("enter the name:-  ")
        self.lastname=input("enter the name:- ")
class Person2(Person):
    def B (self):
        self.name1 = input("enter the name:-  ")
        self.lastname1 = input("enter the name:- ")
        print("person 1 name:_"  ,self.name,   self.lastname )
        print("person 1 lover name :_ ", self.name1, self.lastname1)
p=Person2()
p.A()
p.B()