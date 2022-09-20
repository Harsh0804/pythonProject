
class A:
    def f1(self):
        print(" this is feature 1 ")
    def f2(self):
        print(" this is feature 2 ")

class B:
    def f3(self):
        print(" this is feature 3 ")
    def f4(self):
        print(" this is feature 4 ")

class C(B,A):
    def f5(self):
        print(" this is feature 5 ")
    def f6(self):
        print(" this is feature 6 ")


c1=C()
c1.f1()
c1.f2()
c1.f3()
c1.f4()
c1.f5()
c1.f6()