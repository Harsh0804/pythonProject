class student():
    def __init__(self,sname,sroll,smob,scourse):
        self.sname=input(" enter the name:- ")
        self.sroll=int(input(" enter the roll no :-  "))
        self.smob= int(input(" enter the mobile number  :- "))
        self.scourse= input(" enter the course name :-  ")

    def config(self):
        print("config is :-",self.sname,self.sroll,self.smob,self.scourse)

ss=student()
ss.config()