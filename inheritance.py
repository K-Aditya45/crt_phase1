
#single inheritance
class A:
    def a(self):
        pass
    def b(self):
        pass
class B(A):
    def a(self):
        pass
q=A()
w=B()
w.a()          #def a accessed in by object is the function in the class of B because it has its own priority


#multiple Inheritance
class A:
    def a(self):
        pass
    def b(self):
        pass
class B:
    def a(self):
        pass
    def b(self):
        pass
class C(A,B):
    def e(self):
        pass

q=A()
w=B()
r=C()
r.a()      #r.a is the function of classA because we get inheritance in the way of class c(A,B)

class A:
    def a(self):
        pass
    def b(self):
        pass
class B:
    def a(self):
        pass
    def b(self):
        pass
class C(B,A):
    def e(self):
        pass

q=A()
w=B()
r=C()
r.a()    #r.a is the function of claasB because we get inheritance in the way of class C(B,A)

