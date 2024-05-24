# class student:
#     def s1(self):
#         print("xgcug")
# s=student()
# s.s1()
# student.s1(s) #calling with class

# #constructor 
# class student:
#     def __init__(self) -> None:
#         print("constructor")
#     def s1(self):
#         print("xgcug")
# s=student(2)

# class A:
   
#     def __init__(self,a,b) -> None:       
#           self.a=a
#           self.b=b
#           print(a,b)
#     def hi(self,a,b):
#         print(a,b)
# p=A(1,2)
# p.hi()
    
#polymorphism
class student:
    def __init__(self,a,b):
        self.a=a
        self.b=b                
    def __init__(self,a,b):  #polymorphism is not supported in python inorder write overriding must be done
        print("h hvfhv")
    def printing(self):
        print(self.a,self.b)
    def printing(self):
        print(self.a,self.b) 
A=student(2,3)
A.printing()
# A.printing(4,5)       #once do