#if we want to do a variable or function private just add one underscore before that _fun(),_a
class A:
    def a(self):
        print("hi")
    def b(self):
        print("hello")
       
class B(A):
    def c(self):
        print("how")
    def d(self):
        print("are you")
    
q=A()
w=B() 


#accssing using super
# class A:
#     def __init__(self):
#         print("hi")
#     def _a(self):
#         print("hello")
# class B(A):
#        def __init__(self):
#         print("hi")    
#         super().__init__()
#         super()._a()
# q=A()
# w=B()
# q.a()
# w.a()
 
class A:
    def __init__(self):
        print("hi")
    def a(self):
        print("hello")
class B():
       
    def __init__(self):
        print("hi") 
    def q(self):
        x=A() 
        x.a()
       
w=B()
# q.a()
w.q()