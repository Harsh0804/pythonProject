class A:
    def a():
        print(" Hello Students")
class B(A):
    def b():
        print(" Welcome")
class C(B):
    def c():
        print(" TO second home")

c1=C
c1.a()
c1.b()
c1.c()

