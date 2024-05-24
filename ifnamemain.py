#if we want to do a variable or function private just add one underscore before that _fun(),_a
class A:
    def a(self):
        print("hi")
    def b(self):
        print("hello")
class B:
    def c(self):
        print("how")
    def d(self):
        print("are you")
q=A()
w=B()              