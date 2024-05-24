# def fun(s):
#     return s.upper()
# x=fun
# print(x("kjvnfibh"))

# def fun():
#     print("hi")
# a=fun
# print(a())

# def u(s):
#     return s.upper
# def sm(s):
#     return s.lower()
# def abc(func,s):
#     return func(s)
# print(abc(u,"hvdhv"))
# print(sm,"svcshuggs")

# def fun(s):
#     def cont(a):
#         return s+a
#     return cont   #try with 3 arguments
# x=func("hvb")
# print(x("cjsbc"))   


def decorater(func):
    def inner():
        print("abc")
        func()
        print("gcdgc")
    return inner    
def x():
    print("bcejb")
i=decorater(x)
i()

def decorator(func):
    def inner(a,b):
        if b==0:
            raise Exception('zero')
        func(a,b)
@decorator
 def x(a,b) :
    print(a/b) 
x(3,0)    