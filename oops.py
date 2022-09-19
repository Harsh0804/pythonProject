class Student():
    def __init__(self):
        self.sname=input(" enter the name:- ")
        self.sroll=int(input(" enter the roll no :-  "))
        self.smob= int(input(" enter the mobile number  :- "))
        self.scourse= input(" enter the course name :-  ")

    def details(self):
        print("Details are  :-",self.sname,self.sroll,self.smob,self.scourse)

ss=Student()
ss.details()