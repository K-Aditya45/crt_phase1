class D:
    startinglvl=0
    def gamer(self,lvl):
        a="free"
        self.lvl=lvl
        print(self.startinglvl,a,self.lvl)
f=D()
f.gamer(69)


# class a:
#     abc=10
#     def fun1(self):
#         a=1
#         self.b=2
#         print(a,self.b,self.abc)
#     def fun2(self):
#         print(self.b)    

# s=a()
# a.fun1(8)

# a.fun2()


# from dataclasses import dataclass
# @dataclass()
# class d:

#     star:int=4
#     n:int=0
# D=d()
# print(d.star,d.n) 


class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

        
o1=Node(1)
o2=Node(2)
o3=Node(3)

o1.next=o2
o2.next=o3
print(o1.data)
print(o1.next.data)
print()


    